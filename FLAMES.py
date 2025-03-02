def remove_matching_characters(n1,n2):
    n1 = n1.lower()
    n2 = n2.lower()
    for char in n1:
        if char in n2:
            n1 = n1.replace(char,'',1)
            n2 = n2.replace(char,'',2)
    return n1,n2
def flames_results(n1,n2):
    relation = "FLAMES"
    result_map = { 'F':'Friend','L':'Lover','A':'Attraction','M':'Marriage','E':'Enemy','S':'Siblings'}
    n1,n2 = remove_matching_characters(n1,n2)
    count = len(n1)+len(n2)
    if count == 0:
        print("Names are identical,please enter different names")
    while len(relation)>1:
        index = (count % len(relation))-1
        if index >= 0:
            relation = relation[:index] + relation[index + 1:]
        else:
            relation = relation[:len(relation)-1]
    return result_map[relation]
if __name__ == "__main__":
    print("Welcome to the FLAMES game!")
    n1 = input("Enter the first name:")
    n2 = input("Enter the second name:")
    print("Interesting")
    result = flames_results(n1,n2)
    print("The relationship between",n1,"and",n2,"is",result)