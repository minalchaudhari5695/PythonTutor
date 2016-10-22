""" add three dictionaries into another dictionary """
__author__='minal' 
def main():
    dict1={1:100,2:200}
    dict2={3:300,4:400}
    dict3={5:500,6:600}
    dict_output=dict()
    for dict_element in (dict1,dict2,dict3):
        dict_output.update(dict_element)

    print dict_output

if __name__=='__main__':
    main()

