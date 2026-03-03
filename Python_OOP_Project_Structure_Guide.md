# The Complete Guide to Structuring Python OOP Projects

## Part 1: WHAT IS IT?

### Definition
**Project Structure** is the organized blueprint of how your code is divided into files, folders, classes, and modules. It's the skeleton that holds your application together.

**Architecture** is the high-level design decisions about how different parts of your application communicate and work together.

Think of it like building a house:
- **Structure** = Where are the bedrooms, kitchen, bathrooms? What walls support what?
- **Architecture** = How does water flow? Where are electrical lines? How is HVAC distributed?

---

## Part 2: WHY IS IT NEEDED?

### The Real Benefits (Not Just Theory)

#### 1. **Scalability**
- You start with 1,000 lines. Without structure, your next 5,000 lines become a nightmare.
- With structure, adding 50,000 lines follows the same pattern you established.

#### 2. **Maintainability**
- 6 months later, you'll forget your own code.
- A well-structured project lets you (or others) find and modify code without breaking everything.

#### 3. **Testing**
- Loosely coupled code = easy to test individual components.
- Tightly coupled code = testing one thing requires testing everything.

#### 4. **Collaboration**
- Multiple developers working on the same project.
- Structure prevents merge conflicts and allows parallel development.

#### 5. **Reusability**
- Well-organized classes and modules can be reused in other projects.
- Poorly structured code is locked to one project.

#### 6. **Performance & Optimization**
- Clear separation lets you identify bottlenecks easily.
- Monolithic code = hunting for problems in darkness.

---

## Part 3: THE PROBLEMS YOU'RE FACING

### Common Scenarios (You've Probably Done These)

```
❌ Problem 1: "Where should this function go?"
   - You create a Utils class with 200 random methods
   - Later you can't find anything

❌ Problem 2: "This class does too much"
   - A User class handles validation, database, email, and auth
   - One change breaks everything

❌ Problem 3: "What's my project structure?"
   - Everything in one folder or random folders
   - No clear entry point or organization

❌ Problem 4: "I don't know what's public vs private"
   - No clear API boundaries
   - People (or you) use internal methods meant to be private

❌ Problem 5: "Dependencies are everywhere"
   - Class A imports Class B, which imports Class C, which imports Class A
   - Circular imports and chaos

❌ Problem 6: "How do I organize large projects?"
   - One project structure that works fine at 1,000 lines fails at 50,000 lines
   - Refactoring becomes impossible
```

### Root Cause
You're missing a **mental model** for making these decisions systematically.

---

## Part 4: THE HOW - Your Decision-Making Framework

### Step 1: Start with the Problem Domain

Before writing a single line of code, ask yourself:

#### 1A: What is this project about? (Domain Understanding)

```python
# Example: Building a Library Management System

DOMAIN ELEMENTS:
- Books (physical items with properties)
- Members (people who borrow books)
- Borrowing Process (rules and tracking)
- Fines (late return penalties)
- Inventory (stock management)
```

#### 1B: What are the main "entities" or "concepts"?

These naturally become your primary classes:

```python
# From the domain above, your entities:

class Book:
    """Represents a physical book in the library"""
    pass

class Member:
    """Represents a library member"""
    pass

class BorrowingRecord:
    """Tracks when books are borrowed and returned"""
    pass

class Library:
    """The main orchestrator - manages books, members, borrowing"""
    pass
```

### Step 2: The Single Responsibility Principle (SRP)

#### What It Means
Each class should have **ONE reason to change**.

#### How to Apply It

```python
# ❌ BAD: Multiple reasons to change
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def save_to_database(self):
        # Reason to change: Database schema changes
        pass
    
    def send_email(self):
        # Reason to change: Email service provider changes
        pass
    
    def validate_email(self):
        # Reason to change: Email validation rules change
        pass
```

**Problems:**
- If email service breaks, you modify User class
- If database schema changes, you modify User class
- If validation rules change, you modify User class
- Testing becomes complex (need to mock email, database, etc.)

```python
# ✅ GOOD: Single responsibility per class

class User:
    """Manages user data ONLY"""
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def get_info(self):
        return {"name": self.name, "email": self.email}


class EmailValidator:
    """Only validates emails"""
    @staticmethod
    def is_valid(email):
        return "@" in email and "." in email


class UserRepository:
    """Only handles database operations"""
    def save(self, user):
        # Database logic here
        pass
    
    def find_by_id(self, user_id):
        # Database logic here
        pass


class EmailService:
    """Only handles email sending"""
    def send(self, email, message):
        # Email sending logic here
        pass
```

**Benefits:**
- User class only changes if user data structure changes
- Easy to test each class independently
- Easy to swap database or email provider

### Step 3: Dependency Injection (Loose Coupling)

#### The Problem
```python
# ❌ BAD: Library class tightly coupled to FileRepository

class FileRepository:
    def save(self, data):
        with open('data.txt', 'w') as f:
            f.write(data)

class Library:
    def __init__(self):
        self.repository = FileRepository()  # ❌ HARD DEPENDENCY
    
    def add_book(self, book):
        self.repository.save(book.to_string())
```

**Why it's bad:**
- Want to use DatabaseRepository? Must change Library class
- Can't test Library without FileRepository
- Adding logging requires changing Library

#### The Solution
```python
# ✅ GOOD: Library depends on an INTERFACE, not concrete class

from abc import ABC, abstractmethod

class IRepository(ABC):
    """Interface that any repository must follow"""
    @abstractmethod
    def save(self, data):
        pass

class FileRepository(IRepository):
    def save(self, data):
        with open('data.txt', 'w') as f:
            f.write(data)

class DatabaseRepository(IRepository):
    def save(self, data):
        # Database logic
        pass

class Library:
    def __init__(self, repository: IRepository):
        """Inject the dependency - don't create it"""
        self.repository = repository
    
    def add_book(self, book):
        self.repository.save(book.to_string())

# Usage - extremely flexible
file_repo = FileRepository()
library1 = Library(file_repo)

db_repo = DatabaseRepository()
library2 = Library(db_repo)
```

**Benefits:**
- Library doesn't care what type of repository is passed
- Easy to test with a MockRepository
- Easy to switch implementations

### Step 4: Project Directory Structure

#### Basic Structure (Small Projects < 5,000 lines)

```
my_project/
├── main.py                 # Entry point
├── requirements.txt        # Dependencies
├── README.md              # Documentation
├── .gitignore             # Git ignore file
├── models/                # Your domain classes
│   ├── __init__.py
│   ├── user.py
│   ├── book.py
│   └── order.py
├── repositories/          # Data access layer
│   ├── __init__.py
│   ├── user_repository.py
│   └── book_repository.py
├── services/              # Business logic layer
│   ├── __init__.py
│   ├── user_service.py
│   └── book_service.py
├── utils/                 # Utilities and helpers
│   ├── __init__.py
│   ├── validators.py
│   └── formatters.py
└── tests/                 # Test files
    ├── __init__.py
    ├── test_user.py
    └── test_book.py
```

#### Medium Structure (5,000 - 50,000 lines)

```
my_project/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── config/                # Configuration
│   ├── __init__.py
│   ├── settings.py
│   └── constants.py
├── src/                   # All source code
│   ├── __init__.py
│   ├── domain/            # Core business logic
│   │   ├── __init__.py
│   │   ├── entities/      # Domain objects
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   └── book.py
│   │   └── interfaces/    # Abstract base classes
│   │       ├── __init__.py
│   │       ├── repository.py
│   │       └── service.py
│   ├── infrastructure/    # External dependencies
│   │   ├── __init__.py
│   │   ├── repositories/  # Database operations
│   │   │   ├── __init__.py
│   │   │   ├── user_repository.py
│   │   │   └── book_repository.py
│   │   ├── services/      # External services
│   │   │   ├── __init__.py
│   │   │   ├── email_service.py
│   │   │   └── payment_service.py
│   │   └── database.py    # DB connection
│   ├── application/       # Use cases / Business logic
│   │   ├── __init__.py
│   │   ├── user_use_case.py
│   │   └── book_use_case.py
│   ├── api/               # Web layer (if applicable)
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── schemas.py
│   └── utils/
│       ├── __init__.py
│       └── validators.py
├── tests/
│   ├── __init__.py
│   ├── unit/
│   ├── integration/
│   └── fixtures.py
└── docker/                # Deployment files
    ├── Dockerfile
    └── docker-compose.yml
```

#### Large Structure (50,000+ lines / Microservices)

```
my_project/
├── services/
│   ├── user_service/
│   │   ├── src/
│   │   │   ├── domain/
│   │   │   ├── infrastructure/
│   │   │   └── application/
│   │   ├── tests/
│   │   └── requirements.txt
│   ├── book_service/
│   │   ├── src/
│   │   ├── tests/
│   │   └── requirements.txt
│   └── order_service/
├── shared/                # Shared libraries
│   ├── models/
│   ├── enums/
│   └── exceptions.py
├── scripts/               # Utilities and scripts
├── docker-compose.yml     # Orchestration
└── docs/                  # Documentation
```

### Step 5: The Layered Architecture (Most Important)

This is THE pattern you need to understand. It works for 90% of projects.

```
┌─────────────────────────────┐
│   API / Presentation Layer  │ (Routes, Views, Controllers)
│   (How data comes IN/OUT)   │
└──────────────┬──────────────┘
               │
┌──────────────▼──────────────┐
│  Application Layer          │ (Use Cases, Business Workflows)
│  (WHAT your app does)       │
└──────────────┬──────────────┘
               │
┌──────────────▼──────────────┐
│  Domain Layer               │ (Entities, Business Rules)
│  (Core business logic)      │
└──────────────┬──────────────┘
               │
┌──────────────▼──────────────┐
│  Infrastructure Layer       │ (DB, Email, External APIs)
│  (HOW we access data)       │
└─────────────────────────────┘
```

#### Concrete Example: User Registration

```python
# ============================================
# LAYER 1: DOMAIN (Core Business Rules)
# ============================================

from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class User:
    """Domain Entity - represents a user"""
    id: str
    email: str
    password_hash: str
    
    def is_valid(self) -> bool:
        """Business rule: validate a user"""
        return "@" in self.email and len(self.password_hash) > 0


class IUserRepository(ABC):
    """Interface - any repository must implement this"""
    @abstractmethod
    def save(self, user: User) -> None:
        pass
    
    @abstractmethod
    def find_by_email(self, email: str) -> User | None:
        pass


# ============================================
# LAYER 2: INFRASTRUCTURE (External Dependencies)
# ============================================

import hashlib
from uuid import uuid4

class UserRepository(IUserRepository):
    """Concrete implementation - stores users in database"""
    
    def __init__(self, db_connection):
        self.db = db_connection
    
    def save(self, user: User) -> None:
        self.db.execute(
            "INSERT INTO users (id, email, password_hash) VALUES (?, ?, ?)",
            (user.id, user.email, user.password_hash)
        )
    
    def find_by_email(self, email: str) -> User | None:
        result = self.db.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        ).fetchone()
        
        if result:
            return User(result[0], result[1], result[2])
        return None


class EmailService:
    """Infrastructure - sends emails"""
    
    def send_welcome_email(self, email: str) -> bool:
        # Call external email API
        print(f"Sending welcome email to {email}")
        return True


# ============================================
# LAYER 3: APPLICATION (Business Workflows / Use Cases)
# ============================================

class RegisterUserUseCase:
    """Application layer - orchestrates user registration"""
    
    def __init__(self, user_repository: IUserRepository, email_service: EmailService):
        self.user_repository = user_repository
        self.email_service = email_service
    
    def execute(self, email: str, password: str) -> dict:
        """
        Use case: Register a new user
        
        Steps:
        1. Check if user already exists
        2. Hash password
        3. Create user entity
        4. Save to database
        5. Send welcome email
        6. Return success response
        """
        
        # Step 1: Check existence
        existing_user = self.user_repository.find_by_email(email)
        if existing_user:
            return {"success": False, "error": "User already exists"}
        
        # Step 2: Hash password (domain responsibility)
        password_hash = self._hash_password(password)
        
        # Step 3: Create entity
        new_user = User(
            id=str(uuid4()),
            email=email,
            password_hash=password_hash
        )
        
        # Step 4: Validate (domain rule)
        if not new_user.is_valid():
            return {"success": False, "error": "Invalid user data"}
        
        # Step 5: Persist
        self.user_repository.save(new_user)
        
        # Step 6: Send email
        self.email_service.send_welcome_email(email)
        
        return {"success": True, "user_id": new_user.id}
    
    @staticmethod
    def _hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()


# ============================================
# LAYER 4: API / PRESENTATION (Entry Points)
# ============================================

from flask import Flask, request, jsonify

app = Flask(__name__)

# Dependency Injection - set up at application start
db_connection = None  # Your DB connection
email_service = EmailService()
user_repository = UserRepository(db_connection)
register_use_case = RegisterUserUseCase(user_repository, email_service)


@app.route('/register', methods=['POST'])
def register_user():
    """API endpoint for user registration"""
    data = request.json
    
    result = register_use_case.execute(
        email=data['email'],
        password=data['password']
    )
    
    if result['success']:
        return jsonify({"message": "User registered", "user_id": result['user_id']}), 201
    else:
        return jsonify({"error": result['error']}), 400


if __name__ == '__main__':
    app.run()
```

### Step 6: Making Design Decisions - The Checklist

When deciding on classes and methods, ask yourself:

```
FOR EACH NEW CLASS:

☐ What is its single responsibility?
  (Can I describe it in one sentence without using "and"?)

☐ Does it belong to the domain layer?
  (Is it a core business concept?)

☐ What are its dependencies?
  (Should they be injected?)

☐ Is the interface clear?
  (Would someone know what public methods do?)

☐ Can it be tested in isolation?
  (Can I test it without mocking 10 other classes?)

FOR EACH METHOD:

☐ Does it do one thing?
  (Can I name it with a verb that doesn't contain "and/or"?)

☐ Is it too long? (>30 lines usually means split it)

☐ Does it change state or just return data?
  (If both, consider splitting)

☐ Are parameters clear?
  (More than 3-4 parameters = might need a class)

☐ Should it be public or private?
  (Does external code need to call this?)
```

---

## Part 5: Decision Trees (Fast Reference)

### "Where should this functionality go?"

```
Do I need to fetch/store data?
├─ YES → Infrastructure Layer (Repository)
└─ NO →
    Do I coordinate multiple operations?
    ├─ YES → Application Layer (Use Case)
    └─ NO →
        Is it a core business concept?
        ├─ YES → Domain Layer (Entity)
        └─ NO → 
            Is it a web endpoint?
            ├─ YES → API Layer (Route)
            └─ NO → Utils/Helpers
```

### "Should this be a class?"

```
Can I describe it with a noun?
├─ YES → Probably a class
├─ NO → 
    Is it just behavior (utility function)?
    ├─ YES → Keep it as a function
    └─ NO → Rethink the design
```

### "How many classes do I need?"

```
Start minimal:
- 1 main entity/domain class
- 1 repository
- 1 service
- 1 API route

Add more only when:
- A class is handling multiple responsibilities
- You find yourself with >300 lines in a file
- Testing becomes difficult due to many dependencies
```

---

## Part 6: Real-World Examples

### Example 1: E-Commerce Order System

```python
# DOMAIN
class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
    
    def can_purchase(self, quantity) -> bool:
        return self.stock >= quantity
    
    def apply_discount(self, percentage) -> float:
        return self.price * (1 - percentage / 100)


class Order:
    def __init__(self, order_id, customer_id):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = []
        self.status = "pending"
    
    def add_item(self, product: Product, quantity: int):
        if product.can_purchase(quantity):
            self.items.append({"product": product, "quantity": quantity})
        else:
            raise Exception("Insufficient stock")
    
    def total_price(self) -> float:
        return sum(item["product"].price * item["quantity"] for item in self.items)
    
    def mark_completed(self):
        if self.items:
            self.status = "completed"


# INFRASTRUCTURE
class IOrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order): pass
    @abstractmethod
    def find_by_id(self, order_id: str) -> Order: pass

class OrderRepository(IOrderRepository):
    def __init__(self, db):
        self.db = db
    
    def save(self, order: Order):
        # SQL: INSERT INTO orders ...
        pass
    
    def find_by_id(self, order_id: str) -> Order:
        # SQL: SELECT FROM orders ...
        pass

class PaymentService:
    def process_payment(self, amount: float, card_token: str) -> bool:
        # Call payment gateway
        return True


# APPLICATION
class PlaceOrderUseCase:
    def __init__(self, order_repo: IOrderRepository, payment_service: PaymentService):
        self.order_repo = order_repo
        self.payment_service = payment_service
    
    def execute(self, customer_id: str, products_with_qty: list) -> dict:
        # 1. Create order
        order = Order(str(uuid4()), customer_id)
        
        # 2. Add items
        for product, quantity in products_with_qty:
            order.add_item(product, quantity)
        
        # 3. Process payment
        if not self.payment_service.process_payment(order.total_price(), "token"):
            return {"success": False, "error": "Payment failed"}
        
        # 4. Save order
        self.order_repo.save(order)
        order.mark_completed()
        
        return {"success": True, "order_id": order.order_id, "total": order.total_price()}
```

### Example 2: Blog Application

```python
# DOMAIN
class Post:
    def __init__(self, id, title, content, author_id, created_at):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.created_at = created_at
        self.tags = []
    
    def is_published(self) -> bool:
        return self.content is not None and len(self.title) > 0


class Comment:
    def __init__(self, id, post_id, author_id, content):
        self.id = id
        self.post_id = post_id
        self.author_id = author_id
        self.content = content
        self.created_at = datetime.now()


# INFRASTRUCTURE
class PostRepository:
    def __init__(self, db):
        self.db = db
    
    def save(self, post: Post): pass
    def find_by_id(self, post_id: str) -> Post: pass
    def find_all_by_author(self, author_id: str) -> list[Post]: pass

class CommentRepository:
    def __init__(self, db):
        self.db = db
    
    def save(self, comment: Comment): pass
    def find_by_post_id(self, post_id: str) -> list[Comment]: pass


# APPLICATION
class CreatePostUseCase:
    def __init__(self, post_repo: PostRepository):
        self.post_repo = post_repo
    
    def execute(self, title: str, content: str, author_id: str) -> dict:
        post = Post(str(uuid4()), title, content, author_id, datetime.now())
        
        if not post.is_published():
            return {"success": False, "error": "Invalid post"}
        
        self.post_repo.save(post)
        return {"success": True, "post_id": post.id}


class CommentOnPostUseCase:
    def __init__(self, post_repo: PostRepository, comment_repo: CommentRepository):
        self.post_repo = post_repo
        self.comment_repo = comment_repo
    
    def execute(self, post_id: str, author_id: str, content: str) -> dict:
        post = self.post_repo.find_by_id(post_id)
        
        if not post:
            return {"success": False, "error": "Post not found"}
        
        comment = Comment(str(uuid4()), post_id, author_id, content)
        self.comment_repo.save(comment)
        
        return {"success": True, "comment_id": comment.id}
```

---

## Part 7: Common Mistakes to Avoid

### ❌ Mistake 1: God Classes

```python
# DON'T DO THIS:
class User:
    # 200 methods doing everything
    # Authentication, validation, database, email, logging, etc.
    pass
```

**Fix:** Break into multiple classes - one per responsibility

### ❌ Mistake 2: Circular Dependencies

```python
# DON'T:
# user.py imports order.py
# order.py imports user.py
```

**Fix:** Use interfaces/abstract classes, or restructure to eliminate the cycle

### ❌ Mistake 3: Everything is Public

```python
# DON'T:
class Order:
    def __init__(self):
        self.internal_state = {}  # Looks public, but meant to be private
        self.calculated_tax = 0   # Shouldn't be modified directly
```

**Fix:** Use `_private` naming convention or properties

```python
# DO:
class Order:
    def __init__(self):
        self._internal_state = {}
        self._calculated_tax = 0
    
    @property
    def total(self):
        return self._calculate_total()
    
    def _calculate_total(self):
        # Private method
        pass
```

### ❌ Mistake 4: Mixing Layers

```python
# DON'T:
class User:
    def __init__(self, name):
        self.name = name
    
    def save_to_database(self):  # ❌ Infrastructure logic in Domain
        db.execute("INSERT...")
    
    def send_email(self):  # ❌ Infrastructure logic in Domain
        smtp.send(...)
```

**Fix:** Keep Domain pure, inject infrastructure

### ❌ Mistake 5: Too Many Constructor Parameters

```python
# DON'T:
class OrderService:
    def __init__(self, repo1, repo2, service1, service2, service3, config1, config2):
        pass
```

**Fix:** Use a factory or configuration object

```python
# DO:
class OrderServiceFactory:
    def create(self):
        config = Config()
        repos = RepositoryCollection()
        services = ServiceCollection()
        return OrderService(repos, services, config)
```

---

## Part 8: Your First Project Checklist

When starting ANY new project, follow this checklist:

```
STEP 1: UNDERSTAND THE PROBLEM
☐ Write down 3-5 main entities/concepts
☐ Identify 3-5 main use cases ("What can users do?")
☐ Draw a simple diagram on paper

STEP 2: CREATE DOMAIN LAYER
☐ Create entity classes (User, Order, Product, etc.)
☐ Add business rules as methods
☐ Define interfaces for repositories

STEP 3: CREATE INFRASTRUCTURE LAYER
☐ Implement repository classes
☐ Set up database/file storage
☐ Create external service wrappers (Email, Payment, etc.)

STEP 4: CREATE APPLICATION LAYER
☐ Create Use Case classes for each main workflow
☐ Each UseCase handles one business operation
☐ Use dependency injection

STEP 5: CREATE API/PRESENTATION LAYER
☐ Create routes/endpoints
☐ Call appropriate use cases
☐ Return formatted responses

STEP 6: WRITE TESTS
☐ Test domain entities
☐ Mock repositories and test use cases
☐ Test API endpoints

STEP 7: REFACTOR IF NEEDED
☐ Are any classes doing too much?
☐ Are there circular dependencies?
☐ Can any code be reused?
```

---

## Part 9: Quick Reference - Decision Matrix

| Scenario | Where It Goes | Why |
|----------|--------------|-----|
| Validate email format | Domain Entity method | Core business rule |
| Hash a password | Use Case method | Part of registration workflow |
| Save user to database | Infrastructure Repository | Technical concern |
| Send welcome email | Infrastructure Service | External dependency |
| Handle /api/register request | API Layer Route | Entry point |
| Format date for display | Utils/Formatter | Helper function |
| Check business rule (e.g., age > 18) | Domain Entity method | Core logic |
| Call REST API | Infrastructure Service | External system |
| Execute multi-step workflow | Application Use Case | Business process |
| Transform DTO to Entity | Application/API Layer | Data transformation |

---

## Part 10: Your Toolkit (Code Templates)

### Template 1: Domain Entity with Validation

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class DomainEntity:
    """Template for a domain entity"""
    id: str
    created_at: datetime
    
    def is_valid(self) -> bool:
        """Override this with business rules"""
        return len(self.id) > 0
    
    def __post_init__(self):
        """Validate after initialization"""
        if not self.is_valid():
            raise ValueError("Invalid entity")
```

### Template 2: Repository Interface

```python
from abc import ABC, abstractmethod
from typing import Optional, List

class IRepository(ABC):
    """Interface for repositories"""
    
    @abstractmethod
    def save(self, entity) -> None:
        pass
    
    @abstractmethod
    def find_by_id(self, id: str) -> Optional[object]:
        pass
    
    @abstractmethod
    def find_all(self) -> List[object]:
        pass
    
    @abstractmethod
    def delete(self, id: str) -> bool:
        pass
```

### Template 3: Use Case

```python
from abc import ABC, abstractmethod

class UseCase(ABC):
    """Template for use cases"""
    
    @abstractmethod
    def execute(self, **kwargs):
        """
        Business operation
        
        Returns:
            dict with {"success": bool, ...}
        """
        pass
```

### Template 4: API Route

```python
from flask import Blueprint, request, jsonify

bp = Blueprint('module', __name__, url_prefix='/api')

@bp.route('/resource', methods=['POST'])
def create_resource():
    data = request.json
    result = use_case.execute(**data)
    
    if result['success']:
        return jsonify(result), 201
    return jsonify({"error": result.get('error')}), 400
```

---

## Summary: Your Mental Model

When building ANY project, think in layers:

1. **DOMAIN** (What does the business do?)
   - Entities with business rules
   - Interfaces for repositories

2. **INFRASTRUCTURE** (How do we access external systems?)
   - Database repositories
   - Email services
   - API integrations

3. **APPLICATION** (How do we combine domain + infrastructure?)
   - Use cases
   - Business workflows

4. **API** (How do users interact?)
   - Routes/endpoints
   - Request/response handling

**Golden Rules:**
- One responsibility per class
- Inject dependencies
- Keep domains pure (no database/email logic)
- Test each layer independently
- Use interfaces to avoid coupling

Start here with every project, and you'll have a solid foundation.
