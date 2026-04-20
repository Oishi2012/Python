my_dict={1:'apple',2:'orange'}
print(my_dict)

student={'name':'Mira','class':'7','roll':'two'}
print(student)
print(student.get('name'))
# Update a value
student['class']=8
print(student)

# Add a value
student['phone']=99945489953
print(student)

# Remove a particular Elemant
student.pop('class')
print(student)
