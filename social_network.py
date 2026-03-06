from __future__ import annotations


class User:
  def __init__(self, name:str):
    self.name = name
    self.followers:list[User] =[]
    self.following:list[User] = []
    self.messages:list[Message] = []

  def follow(self, user:User):
    if user in self.following:
      raise ValueError(f"{self.name} is already following {user.name}.")

    if user is self:
      raise ValueError("You can't follow yourself.")

    self.following.append(user)
    user.followers.append(self)
    
  def send_message(self, recipient: User, content: str, timestamp: str):
    msg = Message(sender=self, recipient=recipient, content=content, timestamp=timestamp)
    self.messages.append(msg)          
    recipient.messages.append(msg) 
  
  def __repr__(self):
    return f"User(name={self.name!r}, following={len(self.following)}, followers={len(self.followers)})"

class Message:
  def __init__(self, sender: User, recipient: User, content: str, timestamp: str):
      self.sender = sender
      self.recipient = recipient
      self.content = content
      self.timestamp = timestamp

  def __repr__(self):
      return f"Message(from={self.sender.name!r}, to={self.recipient.name!r}, content={self.content!r}, at={self.timestamp!r})"

if __name__ == "__main__":
  alice = User("Alice")
  bob = User("Bob")
  charlie = User("Charlie")

  alice.follow(bob)
  alice.follow(charlie)
  bob.follow(alice)

  alice.send_message(bob, "Hello Bob!", "10:00 AM")
  bob.send_message(alice, "Learning OOP!", "10:30 AM")

  print(f"{alice.name} is following:")
  for u in alice.following:
      print(f"  - {u.name}")

  print(f"\n{bob.name}'s followers:")
  for u in bob.followers:
      print(f"  - {u.name}")

  print(f"\n{alice.name}'s messages:")
  for m in alice.messages:
      print(f"  [{m.timestamp}] {m.content}")


  print(alice)
  print(bob)
