import regex as re

def extract_txt_1(text):
    lextd=[]
    
    #find the pattern and choos the middle sequence
    
    pattern = r'\[.\](.*?)\.\[.\]'

    matches = re.findall(pattern, text)

    if matches:
        extracted_strings_text= [match.strip('.') for match in matches]
        
        #print(extracted_strings_text[0])

        lextd.extend(str(extracted_strings_text[0]))
        return lextd
    else:
        print("No match found.")
        return "No match found."

#test extract_txt
extract_txt_1("[R].LTTDSRHYFCREVAPPR.[L]")

#Function to find the index
def extract_index(index):
    pattern_index = r'\[(\d+-\d+)\]'

    # Extracting the desired portion using regex
    match_index = re.search(pattern_index, index)
    if match_index:
        extracted_string_index = match_index.group(1)
        #print(extracted_string_index)
        return extracted_string_index
    else:
        print("No match found.")
        return "No match found."

#test extract_index
extract_index('JAK3 [351-367]')


#This function is to remove the dash
def split_the_index_numbers(indx):
    no_dash=indx.split('-')
    no_dash_to_int = list(map ((lambda x : int(x)) , no_dash))
    return no_dash_to_int


#test split_the_index_numbers
split_the_index_numbers('351-367')

#Read in the jason file:
import json
# The address can be changed
f = open("/Users/ramin/Downloads/Amir's Files/JAK3_peptides.json")
data=json.load(f)
#find maximum lenght
def get_max(json_data):
    data_l=[]
    for i in range(len(json_data)):
        i1 = extract_index(data[i]['Location'])
        i2 = split_the_index_numbers(i1)
        for n in i2:
            data_l.append(n)
            #print(data_l)
        #print(i2)
    #print(type(max(data_l)))    
    return(max(data_l))


#designate the lenght of the list
def make_max_list(number):
    seqeuence_list= [None]*number
    return seqeuence_list





lst1=make_max_list(1104)
for n in data:
    #extract_txt_1(n['Seq.'])
    lst1[split_the_index_numbers(extract_index(n['Location']))[0] : split_the_index_numbers(extract_index(n['Location']))[1]] = extract_txt_1(n['Seq.'])
    #print(extract_index(n['Location']))

# Test the make_max_list and get_max function
make_max_list(get_max(data))

#for loop for the final result
lst1=make_max_list(get_max(data))
for n in data:
    #extract_txt_1(n['Seq.'])
    lst1[split_the_index_numbers(extract_index(n['Location']))[0] : split_the_index_numbers(extract_index(n['Location']))[1]] = extract_txt_1(n['Seq.'])
    #print(extract_index(n['Location']))