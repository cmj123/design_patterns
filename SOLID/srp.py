# SRC SOC - SRC - Single Responsibility Principle & Seperation of concerns
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}:{text}")
        

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # # Function to save file
    # """
    #  The journal now has persistant functionality
    #  Terrible idea to have both entry functionality with persistant functionality
    #     Because you dont want every class to have its own save method
    #     You have to go into each file and change the save method (persistant method)
    #     In a big project, it is painful!!!!
        
    # """
    # def save(self, filename):
    #     file = open(filename, 'w')
    #     filename.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def low_from_web(self, uri):
    #     pass 

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry('I laughed together')
j.add_entry('I ate a burger')
# print(f'Journal entries:\n{j}')


file = "journal.txt"
PersistenceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())