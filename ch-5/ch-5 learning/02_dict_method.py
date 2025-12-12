marks = {
         "ravi":60,
         "shubham":77,
         "rakul":33
      

}
#print (marks.items())

#print(marks.keys())
#print(mrks.item())

print(marks.values())

marks.update({"ravi":56, "raman deep":76})#their using for updating 
print(marks)

sessional1 = {"ravi":40,"vinod":40}
sessional2 ={"ravi":36,"vinod":55,"gautam":46}


F_sessional = sessional1.copy()
print(F_sessional)

merged_sessional = {**sessional1, **sessional2}
print(merged_sessional)

#print(marks.get("rakul")) Return None
#print(marks["Rakul"]) Return Error