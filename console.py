from models.staff import Staff
import repositories.staff_repository as staff_repository

staff_repository.delete_all()

staff1 = Staff('Ada','08/08/2020','food',4)
staff_repository.save(staff1)
staff2 = Staff('Eve','09/10/2020','Health',5)
staff_repository.save(staff2)

