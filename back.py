
class work_manager:
    def __init__(self):
        self.work_list = []
        self.worklist_current = 0
        self.workdata_count = 0
        self.worklist_count = 0

    def print_menu(self):
        print("1. add new work")
        print("2. delete work")
        print("3. show work lists")
        print("4. select work")
        print("---------------------")
        try:
            print(f"current work: {self.work_list[self.worklist_current]["work_name"]}")
        except IndexError:
            print(f"current work: {self.worklist_current}")
        print("5. add new data")
        print("6. delete data")
        print("7. show all data")

    def add_worklist(self, work_name, work_data = [], worklist_count = 0):
        work = {"work_name": work_name, "work_data": work_data, "worklist_count": worklist_count}
        self.work_list.append(work)
        self.worklist_count += 1

    def delete_worklist(self, index):
        if self.work_list:
            del self.work_list[index]

    def show_worklists(self):
        for i in range(len(self.work_list)):
            print(f"work name: {self.work_list[i]["work_name"]}  |  work_data: {self.work_list[i]["work_data"]}  |  work_count: {self.work_list[i]["work_count"]}")

    def select_work(self):
        for i in range(len(self.work_list)):
            print(f"{i + 1}. {self.work_list[i]["work_name"]}")        
        self.worklist_current = int(input("enter work index: ")) - 1

    def add_workdata(self, mm, mm_addr,twitter):
        workdata = {"metamask": mm, "metamask_addr": mm_addr,"twitter": twitter}
        self.work_list[self.worklist_current]["work_data"].append(workdata)
        self.workdata_count += 1
        print(self.work_list[self.worklist_current]["work_data"])

    def delete_workdata(self, index):
        del self.work_list[self.worklist_current]["work_data"][index]
        self.workdata_count -= 1

    def show_workdata(self):
        for i in self.work_list[self.worklist_current]["work_data"]:
            print(f"metamask: {i["metamask"]}  | metamask address: {i["metamask_addr"]} |  twitter: {i["twitter"]}")


    

    
m = work_manager()

def main():
    m.print_menu()
    a = input("enter your choice: ")

    match a:
        case "1": 
            name = input("enter work name: ")
            m.add_worklist(name)
        case "2":
            index = int(input("enter index of list: "))
            m.delete_worklist(index)
        case "3":
            m.show_worklists()
        case "4":
            m.select_work()
        case "5":
            mm, mm_addr, twitter = input("enter mm phrase: "), input("enter mm address: "), input("enter twitter cookie: ")
            m.add_workdata(mm, mm_addr, twitter)
        case "6":
            index = int(input("enter index of workdata: "))
            m.delete_workdata(index)
        case "7":
            m.show_workdata()            
        case _:
            print("low iq")



if __name__ == "__main__":
    while True:
        main()