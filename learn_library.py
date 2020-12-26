from os import system, getcwd
import shutil


class Library:
    """Library class """
    def __init__(self):
        self.libCode = self.title = self.price = ''
        self.fileName = ''

    def lib_method(self):
        """Enter common details for books and software"""
        self.libCode = input("Enter the library code :")
        self.title = input("Enter the title :")
        self.price = input('Enter the price :')
        return self.libCode , self.title, self.price

    def empty_file_method(self,file_name):
        """Delet all books and software records"""
        self.file = open(file_name,'a')
        self.file.seek(0,2) # goes to the end of file
        self.fil_len = self.file.tell() # stor the lenght of file
        if self.fil_len == 0:
            print('*****************************')
            print('*****************************')
            print('******File already empty ****')
            print('*****************************')
            print('*****************************')
        else:
            self.file.truncate(0) # Empty the file if the length of file file is not zero
        if file_name =='BookDetails': # checks if the filename is bookdetails
            print('*****************************')
            print('*****************************')
            print('***All book records deleted**')
            print('*****************************')
            print('*****************************')
        else:
            print('*****************************')
            print('*****************************')
            print('*All software records deleted*')
            print('*****************************')
            print('*****************************')
            self.file.close()

    def clear_screen_method(self):
        """Clear screen method =>> clear the screen"""
        self.keyInput = 0
        while not self.keyInput:
            print('what')
            self.ch = input('Press entry to continue ...')
            if self.ch!='':
                print('Wrong key pressed !! pleas press entry key')
            else:
                self.clearscreen = system('clear')
                self.keyInput = 1

class Books(Library):
    """Books class"""
    def __init__(self):
        """Class books constructor"""
        Library.__init__(self)
        self.auther = self.publisher = self.page_count = self.isbn = '' # initialise attributes of the books

    def bksMethod(self): # Takes input for book details
        """Entry books details"""
        self.bk_file = open('BookDetails','a') # Creat and open a file in append mode
        self.lib_m = self.lib_method() # Calls the method of the base class, which takes input for three attributes
        # lib_code, title and price
        self.bk_file.write(self.lib_m[0]+',')
        self.bk_file.write(self.lib_m[1]+',')
        self.auther = input('Enter the name of auther :')
        self.bk_file.write(self.auther + ',')
        self.publisher = input('Enter the name of publisher :')
        self.bk_file.write(self.publisher + ',')
        self.isbn = input('Enter the isbn :')
        self.bk_file.write(self.isbn + ',')
        self.page_count = input('Enter the page count :')
        self.bk_file.write(self.page_count + ',')
        self.bk_file.write(self.lib_m[2] + '\n')
        self.bk_file.close()
        print('''You have enterd the following details for a book:
        =========================================================
              library code : {}
              title : {}
              author : {}
              publisher : {}
              isbn : {}
              page count : {}
              price : {}
              '''.format(self.lib_m[0],self.lib_m[1],self.auther,self.publisher,self.isbn,self.page_count,self.lib_m[2]))

    def book_search(self):
        """Search for book record"""
        self.bk_det = open('BookDetails', 'r')
        self.bk_det.seek(0,2)
        self.bk_file_len = self.bk_det.tell()
        if self.bk_file_len == 0:
            print('*****************************')
            print('*****************************')
            print('***No records available *****')
            print('*****************************')
            print('*****************************')
            self.bk_det.close()
        else:
            self.bk_det = open('BookDetails', 'r')
            self.lines = self.bk_det.readlines()
            self.size = len(self.lines)
            self.name = input('Enter name of book :')
            i = 0
            self.reco = ''
            while i < self.size:
                self.line = self.lines[i]
                self.fd = self.line.find(self.name)
                if self.fd > 0:
                    self.reco = self.line.split(',')
                    print('''
                    View deatils for a book:
                    ==================================================
                    library code : {}
                    title : {}
                    author : {}
                    puplisher : {}
                    isbn : {}
                    page coun :{}
                    price : {}
                    '''.format(self.reco[0],self.reco[1],self.reco[2],self.reco[3],self.reco[4],self.reco[5],self.reco[6]))
                    i += 1
                else:
                    print('No record avilable')

    def book_delet(self):
        """Delete enty form book library"""
        self.bk_det = open('BookDetails','r')
        self.lines = self.bk_det.readlines()
        self.bk_det.close()
        self.name = input('Enter name of book')
        i = 0
        self.size = len(self.lines) # get size lines lenght
        while i < self.size:
            fd = self.lines[i].find(self.name) # search in line
            if fd > 0:
                del self.lines[i]
                break
            else:
                if i == self.size - 1:
                    print('No record availibal')
            i +=1
        bk_det= open('BookDetails','w')
        bk_det.writelines(self.lines)
        bk_det.close()


class Software(Library):
    """Software Class"""
    def __init__(self):
        "Software"
        Library.__init__(self)
        self.product_of = self.nmb_cd = ''

    def softw_method(self): # takes input for software details
        "Enter software details"
        self.sw_file = open('softwareDetails','a')
        self.lib_m = self.lib_method()
        self.sw_file.write(self.lib_m[0]+',')
        self.sw_file.write(self.lib_m[1]+',')
        self.product_of = input('Enter the name of the software vendor')
        self.sw_file.write(self.product_of + ',')
        self.nmb_cd = input('Enter the number of cd :')
        self.sw_file.write(self.nmb_cd + ',')
        self.sw_file.write(self.lib_m[2]+'\n')
        self.sw_file.close()

        print("""
            you have enterd the following details for a software:
            ===================================================================
            library code : {}
            title : {}
            vendor : {}
            number of cd : {}
            price : {}
        """.format(self.lib_m[0],self.lib_m[1],self.product_of,self.nmb_cd,self.lib_m[2]))

    def sfw_search(self):
        'Search for software record'
        self.sw_file = open('softwareDetails','r')
        self.sw_file.seek(0,2)
        self.sw_file_len = self.sw_file.tell()
        if self.sw_file_len == 0:
            print('*****************************')
            print('*****************************')
            print('***No records available *****')
            print('*****************************')
            print('*****************************')
            self.sw_file.close()
        else:
            self.sw_file = open('softwareDetails','r')
            self.lines = self.sw_file.readlines()
            self.size = len(self.lines)
            self.name = input('Enter name of record :')
            i = 0
            self.reco = ''
            while i < self.size:
                self.line = self.lines[i]
                self.fd = self.line.find(self.name)
                if self.fd > 0:
                    self.reco = self.line.split(',')
                    print('''
                        library code " {}
                        title : {}
                        vendor : {}
                        number of cd : {}
                        price : {}
                    '''.format(self.reco[0],self.reco[1],self.reco[2],self.reco[3],self.reco[4]))
                    i +=1
                else:
                    print('No record avalibale')
    def sfw_delete(self):
        """Delete entey from book library"""
        self.sw_file = open('softwareDetails','r')
        self.lines = self.sw_file.readlines()
        self.sw_file.close()
        self.name = input('Enter name of software :')
        i = 0
        self.size = len(self.lines)
        while i < self.size:
            self.fd = self.lines[i].find(self.name)
            if self.fd > 0:
                del self.lines[i]
                break
            else:
                if i == self.size -1:
                    print('No record availibal')
            i +=1
        self.sw_file = open('softwareDetails','w')
        self.sw_file.writelines(self.lines)
        self.sw_file.close()


class Root (Books,Software):
    """Class root"""
    def __init__(self):
        Books.__init__(self)
        Software.__init__(self)
        self.mpass = ''

    def pass_method(self):
        self.root_file = open('root_sys','a')
        self.root_file.seek(0,2)
        self.f_len = self.root_file.tell()
        if self.f_len == 0:
            print('********* Password *********')
            self.mpass = input('Please enter a password :')
            self.root_file.write(self.mpass)
            self.root_file.close()
            return 1
        else:
            self.root_file = open('root_sys','r')
            self.ps = self.root_file.read()
            self.rpass = input('Enter the password :')
            self.root_file.close()
            if self.rpassss == self.ps:
                return 1
            else:
                print('Wrong password')

    def change_pass(self):
        self.root_file = open('root_sys','a+')
        self.old_pass = self.root_file.readline()
        self.tmp = input('Enter the old password :')
        if self.tmp == self.old_pass:
            self.root_file.truncate(0)
            self.root_file.close()
            self.mpass = input('Please the new password :')
            self.root_file = open('root_sys', 'w')
            self.root_file.write(self.mpass)
            self.root_file.close()
        else:
            print('Wrong password')

    def backup(self):
        """Create a backup copy(file ) """
        print('''
            Create a backup copy to :
            1 - Books file
            2 - Software file
        ''')

        self.choise = input('Enter your choice 1 or 2 :')
        if self.choise == "1":
            self.file = open('BookDetails','r')
            self.dst = getcwd()
            self.file.close()
            self.path = input('Enter the coplete path ')
            try:
                self.path_dst = self.dst + '/BookDetails'
                shutil.copyfile(self.path_dst,self.path)
            except Exception as e:
                print(e)
        if self.choise == '2':
            self.file = open('softwareDetails','r')
            self.dst = getcwd()
            self.file.close()
            self.path = input('Enter the complete path')
            try:
                self.path_dst = self.dst + '/softwareDetails'
                shutil.copyfile(self.path_dst, self.path)
            except Exception as e:
                print(e)


def mainMenu():
    """display the main menu , takes input for choice self"""
    menu_items = """
                    *Main Menu*
        1 - Enter details for books
        2 - Enter details for software
        3 - View details of books
        4 - View details of software
        5 - Delete a record -book-
        6 - Delelte a record -software-
        7 - * Root *
        8 - Quit
        Enter choice (1-8):
    """
    done = 0
    while not done:
        menu_choice = input(menu_items)
        clear_screen = system('clear')
        print('You enterd : {}'.format(menu_choice))
        if menu_choice not in '12345678':
            print('Wrong choice. Enter 1,2,3,4,5,6,7,8')
        else:
            if menu_choice =='8':
                done = 1
            if menu_choice == '1':
                print('***Enter book details***')
                bk.bksMethod()
                bk.clear_screen_method()
            if menu_choice == '2':
                print('*** Enter software details ***')
                sw.softw_method()
                sw.clear_screen_method()
            if menu_choice == '3':
                bk.book_search()
                bk.clear_screen_method()
            if menu_choice == "4":
                sw.sfw_search()
                sw.clear_screen_method()
            if menu_choice == '5':
                bk.book_delet()
                bk.clear_screen_method()
            if menu_choice == '6':
                sw.sfw_delete()
                sw.clear_screen_method()
            if menu_choice == '7':
                root.pass_method()
                if root.pass_method() == 1:
                    menu_root = '''
                        1 - Delete all book records
                        2 - Delete all software records
                        3 - Create a backup copy
                        4 - change your password
                        Enter your choice :
                    '''
                    ch = input(menu_root)
                    if ch == '1':
                        bk.empty_file_method('BookDetails')
                        root.clear_screen_method()
                    if ch == '2':
                        sw.empty_file_method('SoftwareDetails')
                        root.clear_screen_method()
                    if ch == '3':
                        root.backup()
                        root.clear_screen_method()
                    if ch == '4':
                        root.change_pass()
                        root.clear_screen_method()
