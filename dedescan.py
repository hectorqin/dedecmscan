from termcolor import cprint
from lib.lib import check

def main():
    title = '''
                                                                                    
        ...                 ...                                                     
        ...                 ...                                                     
        ...                 ...                                                     
        ...                 ...                                                     
        ...                 ...                                                     
   ........  .......   ........   .......   .......    ......    ......   ........  
  ...  .... .... ....  ... ....  .... ...  .... ...   ... ....  ...  ...  .... .... 
 ....  .... ...   ... ...   ...  ...   ... ...       ...   ...  .    ...  ...   ... 
 ....   ... ......... ...   ... ..........  ....     ...           .....  ...   ... 
 ....   ... ...       ...   ... ....         ......  ...        ........  ...   ... 
 ....  .... ...       ...   ... ....            .... ...   ... ....  ...  ...   ... 
  ...  .... ....  ... ....  ...  ...  .... ...   ... ....  ... ....  ...  ...   ... 
  .........  ........  ........   .......  ........   ........  ........  ...   ... 
    .......   .....     .......    .....     .....      ....     ........ ...   ... 

    '''
    author = '''
                                                 
    '''
    cprint(title, "blue")
    cprint(author, "green")

    target = input("Please enter the url you need to detect: ")
    start = check(target)
    start.poc()

if __name__ == '__main__':
    main()
