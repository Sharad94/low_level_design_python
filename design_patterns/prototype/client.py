from student import Student
from intelligent_student import IntelligentStudent
from student_registry import StudentRegistry

s1 = Student(name="Sharad", age=22, batch="Dec Advanced")
is1 = IntelligentStudent(name="Sharad", age=22, batch="Dec Advanced", iq=99)

student_list = [s1, is1]
for s in student_list:
    new_s = s.copy()
    print(id(s))
    print(s)
    print(id(new_s))
    print(new_s)

student_registry = StudentRegistry()
dec_batch_student = Student(batch="Dec Advanced")
student_registry.add_to_registry("dec_batch", dec_batch_student)

dec_batch_intelligent_student = IntelligentStudent(batch="Dec Advanced", iq=50)
student_registry.add_to_registry("dec_batch_intelligent", dec_batch_intelligent_student)

dec_batch_student_proto = student_registry.get_from_registry("dec_batch")
new_dec_batch_student = dec_batch_student_proto.copy()
print(id(dec_batch_student_proto))
print(dec_batch_student_proto)

new_dec_batch_student.set_name("Chandan")
new_dec_batch_student.set_age(23)
print(id(new_dec_batch_student))
print(new_dec_batch_student)

dec_batch_i_student_proto = student_registry.get_from_registry("dec_batch_intelligent")
new_dec_batch_i_student = dec_batch_i_student_proto.copy()
print(id(dec_batch_i_student_proto))
print(dec_batch_i_student_proto)

new_dec_batch_i_student.set_name("Chandan")
new_dec_batch_i_student.set_age(23)
print(id(new_dec_batch_i_student))
print(new_dec_batch_i_student)
