from datetime import datetime

#  Homework 1: ToDo List Application
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = 'Completed' if self.completed else 'Incomplete'
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {status}\n"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_all_tasks(self):
        return self.tasks

    def list_incomplete_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            return True
        return False


# Homework 2: Simple Blog System  
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.timestamp = datetime.now()

    def edit_post(self, new_title, new_content):
        self.title = new_title
        self.content = new_content

    def __str__(self):
        return f"Title: {self.title}\nBy: {self.author}\nDate: {self.timestamp.strftime('%Y-%m-%d %H:%M')}\nContent: {self.content}\n"

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        return self.posts

    def posts_by_author(self, author):
        return [post for post in self.posts if post.author.lower() == author.lower()]

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            del self.posts[index]
            return True
        return False

    def edit_post(self, index, new_title, new_content):
        if 0 <= index < len(self.posts):
            self.posts[index].edit_post(new_title, new_content)
            return True
        return False

    def latest_posts(self, count=5):
        return sorted(self.posts, key=lambda x: x.timestamp, reverse=True)[:count]


# Homework 3: Simple Banking System 
class Account:
    def __init__(self, acc_number, holder_name, balance=0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def transfer(self, amount, recipient_account):
        if self.withdraw(amount):
            recipient_account.deposit(amount)
            return True
        return False

    def __str__(self):
        return f"Account No: {self.acc_number}\nName: {self.holder_name}\nBalance: ${self.balance:.2f}\n"

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.acc_number] = account

    def get_account(self, acc_number):
        return self.accounts.get(acc_number)

    def check_balance(self, acc_number):
        account = self.get_account(acc_number)
        if account:
            return account.balance
        return None

    def display_account(self, acc_number):
        account = self.get_account(acc_number)
        return str(account) if account else "Account not found"


# -------------------- Main CLI Program -------------------- #
def main():
    todo = ToDoList()
    blog = Blog()
    bank = Bank()

    while True:
        print("\n--- MAIN MENU ---")
        print("1. ToDo List")
        print("2. Blog System")
        print("3. Banking System")
        print("0. Exit")
        choice = input("Choose an option: ")

        # ToDo List Menu
        if choice == '1':
            while True:
                print("\n--- ToDo List ---")
                print("1. Add Task")
                print("2. List All Tasks")
                print("3. List Incomplete Tasks")
                print("4. Mark Task as Complete")
                print("0. Back")
                sub = input("Choose: ")

                if sub == '1':
                    title = input("Title: ")
                    desc = input("Description: ")
                    due = input("Due Date: ")
                    todo.add_task(Task(title, desc, due))
                    print("Task added!")
                elif sub == '2':
                    for i, task in enumerate(todo.list_all_tasks()):
                        print(f"\nTask #{i + 1}:\n{task}")
                elif sub == '3':
                    for i, task in enumerate(todo.list_incomplete_tasks()):
                        print(f"\nTask #{i + 1}:\n{task}")
                elif sub == '4':
                    idx = int(input("Enter task number to mark complete: ")) - 1
                    if todo.mark_task_complete(idx):
                        print("Marked as complete.")
                    else:
                        print("Invalid task number.")
                elif sub == '0':
                    break

        # Blog Menu
        elif choice == '2':
            while True:
                print("\n--- Blog System ---")
                print("1. Add Post")
                print("2. List All Posts")
                print("3. Posts by Author")
                print("4. Delete Post")
                print("5. Edit Post")
                print("6. Latest Posts")
                print("0. Back")
                sub = input("Choose: ")

                if sub == '1':
                    title = input("Title: ")
                    content = input("Content: ")
                    author = input("Author: ")
                    blog.add_post(Post(title, content, author))
                    print("Post added!")
                elif sub == '2':
                    for i, post in enumerate(blog.list_all_posts()):
                        print(f"\nPost #{i + 1}:\n{post}")
                elif sub == '3':
                    name = input("Author name: ")
                    for post in blog.posts_by_author(name):
                        print(f"\n{post}")
                elif sub == '4':
                    idx = int(input("Post number to delete: ")) - 1
                    if blog.delete_post(idx):
                        print("Post deleted.")
                    else:
                        print("Invalid post number.")
                elif sub == '5':
                    idx = int(input("Post number to edit: ")) - 1
                    new_title = input("New title: ")
                    new_content = input("New content: ")
                    if blog.edit_post(idx, new_title, new_content):
                        print("Post edited.")
                    else:
                        print("Invalid post number.")
                elif sub == '6':
                    for post in blog.latest_posts():
                        print(f"\n{post}")
                elif sub == '0':
                    break

        # Bank Menu
        elif choice == '3':
            while True:
                print("\n--- Banking System ---")
                print("1. Add Account")
                print("2. Display Account")
                print("3. Check Balance")
                print("4. Deposit")
                print("5. Withdraw")
                print("6. Transfer")
                print("0. Back")
                sub = input("Choose: ")

                if sub == '1':
                    num = input("Account Number: ")
                    name = input("Account Holder Name: ")
                    bal = float(input("Initial Balance: "))
                    bank.add_account(Account(num, name, bal))
                    print("Account added.")
                elif sub == '2':
                    num = input("Account Number: ")
                    print(bank.display_account(num))
                elif sub == '3':
                    num = input("Account Number: ")
                    bal = bank.check_balance(num)
                    print(f"Balance: ${bal:.2f}" if bal is not None else "Account not found.")
                elif sub == '4':
                    num = input("Account Number: ")
                    amt = float(input("Amount to deposit: "))
                    acc = bank.get_account(num)
                    if acc and acc.deposit(amt):
                        print("Deposit successful.")
                    else:
                        print("Error in deposit.")
                elif sub == '5':
                    num = input("Account Number: ")
                    amt = float(input("Amount to withdraw: "))
                    acc = bank.get_account(num)
                    if acc and acc.withdraw(amt):
                        print("Withdrawal successful.")
                    else:
                        print("Insufficient balance or invalid account.")
                elif sub == '6':
                    from_acc = input("From Account: ")
                    to_acc = input("To Account: ")
                    amt = float(input("Amount to transfer: "))
                    acc1 = bank.get_account(from_acc)
                    acc2 = bank.get_account(to_acc)
                    if acc1 and acc2 and acc1.transfer(amt, acc2):
                        print("Transfer successful.")
                    else:
                        print("Transfer failed.")
                elif sub == '0':
                    break

        elif choice == '0':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
