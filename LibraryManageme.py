# Implementation of the Library Management System according to the provided specification.
# This cell defines all classes and runs the sample usage to show the expected output.
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List, Optional

# ===============================
# 1. LibraryItem (Abstract Base)
# ===============================
class LibraryItem(ABC):
    """
    Abstract base class representing a library item.
    Demonstrates Abstraction and Encapsulation with protected attributes and class-level ID counter.
    """
    _id_counter: int = 1  # Class variable for auto-incremented IDs

    def __init__(self, title: str, creator: str, copies: int) -> None:
        self.id: int = LibraryItem._id_counter  # Auto-generated ID
        LibraryItem._id_counter += 1

        # Encapsulation: use "private-ish" attributes where suitable
        self.title: str = title
        self.creator: str = creator
        self.total_copies: int = copies
        self.available_copies: int = copies

    def is_available(self) -> bool:
        """Return True if at least one copy is available."""
        return self.available_copies > 0

    def borrow(self) -> bool:
        """Attempt to borrow an item; decrement available copies if possible."""
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    def return_item(self) -> bool:
        """Return an item; increment available copies up to total copies."""
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False

    @abstractmethod
    def get_item_info(self) -> str:
        """Detailed information string for the item."""
        raise NotImplementedError

    @abstractmethod
    def get_item_type(self) -> str:
        """Return the item type (e.g., Book, DVD)."""
        raise NotImplementedError

    def __str__(self) -> str:
        """User-friendly string representation (title and creator)."""
        return f"{self.title} by {self.creator}"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, creator={self.creator!r})"

    def __eq__(self, other: object) -> bool:
        """Compare items by ID (identity semantics)."""
        if not isinstance(other, LibraryItem):
            return NotImplemented
        return self.id == other.id


# ===============================
# 2. Book
# ===============================
class Book(LibraryItem):
    """Represents a Book item; inherits from LibraryItem (Inheritance, Polymorphism)."""

    def __init__(self, title: str, author: str, copies: int, isbn: str, num_pages: int) -> None:
        super().__init__(title=title, creator=author, copies=copies)
        self.author: str = author              # Alias to creator
        self.isbn: str = isbn
        self.num_pages: int = num_pages

    def get_item_type(self) -> str:
        return "Book"

    def get_item_info(self) -> str:
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"ISBN: {self.isbn}\n"
            f"Pages: {self.num_pages}\n"
            f"Type: {self.get_item_type()}"
        )


# ===============================
# 3. DVD
# ===============================
class DVD(LibraryItem):
    """Represents a DVD item; inherits from LibraryItem (Inheritance, Polymorphism)."""

    def __init__(self, title: str, director: str, copies: int, duration_minutes: int, genre: str) -> None:
        super().__init__(title=title, creator=director, copies=copies)
        self.director: str = director          # Alias to creator
        self.duration_minutes: int = duration_minutes
        self.genre: str = genre

    def get_item_type(self) -> str:
        return "DVD"

    def get_item_info(self) -> str:
        return (
            f"Title: {self.title}\n"
            f"Director: {self.director}\n"
            f"Duration: {self.duration_minutes} minutes\n"
            f"Genre: {self.genre}\n"
            f"Type: {self.get_item_type()}"
        )


# ===============================
# 4. Member (Observer base)
# ===============================
class Member(ABC):
    """
    Base class for Members implementing the Observer interface.
    Demonstrates Encapsulation (with notifications) and Abstraction.
    """
    _id_counter: int = 1
    MAX_BORROW_LIMIT: int = 0  # to be defined by subclasses

    def __init__(self, name: str, email: str) -> None:
        self.member_id: int = Member._id_counter
        Member._id_counter += 1

        self.name: str = name
        self.email: str = email
        self.borrowed_items: List[int] = []
        self._notifications: List[str] = []

    def can_borrow(self) -> bool:
        return len(self.borrowed_items) < self.get_max_borrow_limit()

    def borrow_item(self, item_id: int) -> bool:
        if not self.can_borrow():
            return False
        self.borrowed_items.append(item_id)
        return True

    def return_item(self, item_id: int) -> bool:
        if item_id in self.borrowed_items:
            self.borrowed_items.remove(item_id)
            return True
        return False

    def get_borrowed_count(self) -> int:
        return len(self.borrowed_items)

    @abstractmethod
    def get_max_borrow_limit(self) -> int:
        raise NotImplementedError

    # Observer pattern method
    def update(self, message: str) -> None:
        self._notifications.append(message)

    def get_notifications(self) -> List[str]:
        return list(self._notifications)

    def clear_notifications(self) -> None:
        self._notifications.clear()

    def __str__(self) -> str:
        # Example: "Alice (1)"
        return f"{self.name} ({self.member_id})"


# ===============================
# 5. RegularMember
# ===============================
class RegularMember(Member):
    MAX_BORROW_LIMIT: int = 3

    def __init__(self, name: str, email: str) -> None:
        super().__init__(name, email)

    def get_max_borrow_limit(self) -> int:
        return self.MAX_BORROW_LIMIT


# ===============================
# 6. PremiumMember
# ===============================
class PremiumMember(Member):
    MAX_BORROW_LIMIT: int = 5

    def __init__(self, name: str, email: str, membership_expiry: Optional[str] = None) -> None:
        super().__init__(name, email)
        self.membership_expiry: Optional[str] = membership_expiry

    def get_max_borrow_limit(self) -> int:
        return self.MAX_BORROW_LIMIT


# ===============================
# 7. Library (Singleton + Subject)
# ===============================
class Library:
    """
    Singleton Library that acts as the Subject in the Observer pattern.
    Keeps track of items, members, and waiting lists.
    """
    _instance: Optional["Library"] = None

    def __new__(cls) -> "Library":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Initialize instance attributes on first creation
            cls._instance.items = {}
            cls._instance.members = {}
            cls._instance.waiting_list = {}
        return cls._instance

    # --- Item management ---
    def add_item(self, item: LibraryItem) -> bool:
        if item.id in self.items:
            return False
        self.items[item.id] = item
        return True

    def remove_item(self, item_id: int) -> bool:
        if item_id in self.items:
            # also remove any waiting list entries associated with item
            self.waiting_list.pop(item_id, None)
            del self.items[item_id]
            return True
        return False

    def search_items(self, query: str) -> List[LibraryItem]:
        q = query.lower().strip()
        return [
            item for item in self.items.values()
            if q in item.title.lower() or q in item.creator.lower()
        ]

    def display_all_items(self) -> None:
        if not self.items:
            print("[No items in library]")
            return
        for item in self.items.values():
            prefix = item.get_item_type()
            print(f"{prefix}: {item} (ID: {item.id})")

    # --- Member management ---
    def add_member(self, member: Member) -> bool:
        if member.member_id in self.members:
            return False
        self.members[member.member_id] = member
        return True

    def remove_member(self, member_id: int) -> bool:
        if member_id in self.members:
            # Ensure they return items? For simplicity, allow removal regardless.
            del self.members[member_id]
            # clean up waiting lists
            for wl in self.waiting_list.values():
                wl[:] = [m for m in wl if m.member_id != member_id]
            return True
        return False

    def display_all_members(self) -> None:
        if not self.members:
            print("[No members]")
            return
        for m in self.members.values():
            print(f"{m} - Max: {m.get_max_borrow_limit()} items")

    # --- Borrow / Return ---
    def borrow_item(self, member_id: int, item_id: int) -> bool:
        member = self.members.get(member_id)
        item = self.items.get(item_id)
        if not member or not item:
            return False
        if not member.can_borrow():
            return False
        if item.borrow():
            member.borrow_item(item_id)
            return True
        return False  # not available

    def return_item(self, member_id: int, item_id: int) -> bool:
        member = self.members.get(member_id)
        item = self.items.get(item_id)
        if not member or not item:
            return False
        if member.return_item(item_id):
            if item.return_item():
                # Notify observers if item has become available
                if item.is_available():
                    self.notify_waiting_members(item_id)
                return True
        return False

    # --- Waiting List & Notifications (Observer pattern) ---
    def join_waiting_list(self, member_id: int, item_id: int) -> bool:
        member = self.members.get(member_id)
        item = self.items.get(item_id)
        if not member or not item:
            return False
        wl = self.waiting_list.setdefault(item_id, [])
        if member not in wl:
            wl.append(member)
            return True
        return False

    def leave_waiting_list(self, member_id: int, item_id: int) -> bool:
        wl = self.waiting_list.get(item_id)
        if not wl:
            return False
        before = len(wl)
        self.waiting_list[item_id] = [m for m in wl if m.member_id != member_id]
        return len(self.waiting_list[item_id]) < before

    def get_waiting_list(self, item_id: int) -> List[Member]:
        return list(self.waiting_list.get(item_id, []))

    def notify_waiting_members(self, item_id: int) -> None:
        wl = self.waiting_list.get(item_id, [])
        item = self.items.get(item_id)
        if not item or not wl:
            return
        message = f"'{item.title}' is now available!"
        for member in wl:
            member.update(message)
        # Optional: keep the waiting list intact; specification only asks to notify.

    # --- Dunder for total items ---
    def __len__(self) -> int:
        return len(self.items)


# ===============================
# Sample Usage / Demo
# ===============================
def main():
    print("=" * 70)
    print("LIBRARY MANAGEMENT SYSTEM - DEMO")
    print("=" * 70)

    # Create library (Singleton)
    library = Library()

    # Add books and DVDs
    book1 = Book("Python Crash Course", "Eric Matthes", 2, "978-1593279288", 544)
    book2 = Book("Clean Code", "Robert Martin", 2, "978-0132350884", 464)
    dvd1 = DVD("The Matrix", "Wachowski Brothers", 2, 136, "Sci-Fi")
    dvd2 = DVD("Inception", "Christopher Nolan", 1, 148, "Thriller")

    library.add_item(book1)
    library.add_item(book2)
    library.add_item(dvd1)
    library.add_item(dvd2)

    print(f"\n--- Added Items ---")
    print(f"Book: {book1} (ID: {book1.id})")
    print(f"DVD: {dvd1} (ID: {dvd1.id})")
    print(f"Total items: {len(library)}")

    # Demonstrate Polymorphism - get_item_info()
    print(f"\n--- Polymorphism Demo: get_item_info() ---")
    print(book1.get_item_info())
    print(f"\n{dvd1.get_item_info()}")

    # Add members
    alice = RegularMember("Alice", "alice@email.com")
    bob = PremiumMember("Bob", "bob@email.com")
    charlie = RegularMember("Charlie", "charlie@email.com")

    library.add_member(alice)
    library.add_member(bob)
    library.add_member(charlie)

    print(f"\n--- Added Members ---")
    print(f"{alice} - Max: {alice.get_max_borrow_limit()} items")
    print(f"{bob} - Max: {bob.get_max_borrow_limit()} items")

    # Regular member borrows items (max 3)
    print(f"\n--- Regular Member Borrowing (Max 3) ---")
    library.borrow_item(alice.member_id, book1.id)
    library.borrow_item(alice.member_id, dvd1.id)
    library.borrow_item(alice.member_id, book2.id)
    print(f"Alice borrowed: {alice.get_borrowed_count()}/{alice.get_max_borrow_limit()} items")

    # Try to exceed limit
    success = library.borrow_item(alice.member_id, dvd2.id)
    print(f"Alice trying 4th item: {success} (exceeded limit)")

    # Premium member borrows items (max 5)
    print(f"\n--- Premium Member Borrowing (Max 5) ---")
    library.borrow_item(bob.member_id, dvd2.id)
    print(f"Bob borrowed: {bob.get_borrowed_count()}/{bob.get_max_borrow_limit()} items")
    print(f"'{dvd2.title}' available: {dvd2.available_copies}")

    # Waiting list and Observer pattern
    print(f"\n--- Waiting List & Observer Pattern ---")
    success = library.borrow_item(charlie.member_id, dvd2.id)
    print(f"Charlie trying to borrow '{dvd2.title}': {success} (unavailable)")

    library.join_waiting_list(charlie.member_id, dvd2.id)
    print(f"Charlie joined waiting list")
    print(f"Waiting list size: {len(library.get_waiting_list(dvd2.id))}")

    # Return item - triggers notification
    print(f"\nBob returns '{dvd2.title}'...")
    library.return_item(bob.member_id, dvd2.id)
    print(f"Charlie's notifications: {charlie.get_notifications()}")

    # Search functionality
    print(f"\n--- Search Items ---")
    results = library.search_items("Python")
    print(f"Search 'Python': {len(results)} result(s)")

    results = library.search_items("Matrix")
    print(f"Search 'Matrix': {len(results)} result(s)")

    # Display final state
    print(f"\n--- Final State ---")
    print(f"Total items: {len(library)}")
    library.display_all_items()

    print("\n" + "=" * 70)
    print("DEMO COMPLETED!")
    print("=" * 70)


if __name__ == "__main__":
    main()
