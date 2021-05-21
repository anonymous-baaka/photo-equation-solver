import wolframalpha
import os

def doit(input):
    print("input= ",input)
    #input="x^3+2*x+3=0"
    app_id="<key>"

    client=wolframalpha.Client(app_id)

    res=client.query(input)
    print("res= ",res)
    #ans=next(res.results).text
    #temp
    for ele in res:
        print(ele)

    row=[]
    for ele in res:
        if 'olution' in ele['@title']:
            row.append(ele)
    #print(row)
    subpodlist=[]
    for _row in row:
        subpodlist.append(_row['subpod'])

    print("subpodlist= ",subpodlist)

    answers=[]
    for ele in subpodlist:
        print(type(ele),ele)
        if "<class 'list'>" in str(type(ele)):
            #answers.append(ele.plaintext)
            for inner in ele:
                answers.append(inner.plaintext)
        else:
            answers.append(ele.plaintext)

    for ele in answers:
        print(ele)

    return answers

if __name__ == "__main__":
    #doit("x^2+x=2")
    pass