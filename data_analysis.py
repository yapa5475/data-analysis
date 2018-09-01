#Data Analysis 					#
#Author: Yash Parekh			#
#Langauge: python 				#
#Run: python3 data_analysis.py  #
#################################
import sys
import fractions
import math

def main():
	print('Welcome to the data analysis calculator')

	command = ''
	while (command != 'q'):
		command = input('What are you trying to do? Select option.\n1. Sum\n2. Difference\n3. Multiply\n4. Average\n5. Standard Deviation\n6. Greatest Common Factor\n7. Raise to Power\n8. Is Prime?\n9. Least Common Multiple * Under Construction*\n10. Smallest Number Divisble by 1 to N\n11. Factorial Digit Sum\nq. Quit\nEnter option: ')
		if command == '1':
			print('\nSum - this will return the absolute value of the sum of the numbers.')
			Sum =  0
			num_of_numbers = int(input('How many numbers do you want to add?\t'))

			while num_of_numbers > 0:
				num_to_add = int(input('Number to add: '))
				Sum += num_to_add
				num_of_numbers -= 1
			print('Total = ' + str(Sum) + '\n')
			#return Sum




		if command == '2':
			print('\nDifference - this will return the absolute value of the difference between the two numbers.')
			first_number = int(input('What is the first number?\t'))
			second_number = int(input('What is the second number?\t'))
			Difference = first_number - second_number
			if(Difference < 0):
				Difference *= -1
			print('Difference = ' + str(Difference) + '\n')
			#return Difference

		if command == '3':
			print('\nMultiply - this will return the value of the numbers multiplied')
			#print('Input numbers to multiply one at a time, followed by the * key')

			total = 1
			num_elements_to_multiply = int(input('Enter number of numbers to multiply: '))
			while num_elements_to_multiply > 0:
				number_to_multiply = int(input('Enter number: '))
				total *= number_to_multiply
				num_elements_to_multiply -= 1
			print(total)
			print('\n')


		if command == '4':
			print('\nAverage - this will return the average of the numbers.')
			Sum = 0
			Average = 0
			num_of_numbers = int(input('How many numbers do you want to take the average of?\t'))
			total_numbers = num_of_numbers

			while num_of_numbers > 0:
				num_to_add = int(input('Number to average: '))
				Sum += num_to_add
				num_of_numbers -= 1
			Average = Sum/total_numbers
			print('Average = ' + str(Average) + '\n')
			#return Average


		if command == '5':
			print('\nStandard Deviaion - this will return the standard deviation of the numbers.')

			#1. calculate average
			Sum = 0
			Average = 0
			num_of_numbers = int(input('How many numbers do you want to take the standard deviation of?\t'))
			total_numbers = num_of_numbers

			while num_of_numbers > 0:
				num_to_add = int(input('Number to add: '))
				Sum += num_to_add
				num_of_numbers -= 1
			Average = Sum/total_numbers


			stddev = 0
			count = 0
			while num_of_numbers > 0:
				stddev = stddev + (x-Average)**2
				count += 1
				num_of_numbers -= 1
				count += 1
				
			stddev = stddev/count

		if command == '6':
			print('\nGreatest Common Factor - this will return the GCF of the numbers.')
			print('Currently this feature works with only two numbers')

			num1 = int(input('What is the first number?'))
			num2 = int(input('What is the second number?'))

			if(num1 > num2):
				gcf = num2
			else:
				gcf = num1
			while gcf > 1:
				if num1 % gcf == 0 and num2 % gcf == 0:
					break
				gcf -= 1


			print(gcf)
			print('\n')
			#return gcf

		if command == '7':
			print('\nRaise to power - this will return result of base to power.')
			num1 = int(input('Enter base: '))
			num2 = int(input('Enter power: '))

			result = num1
			while (num2 > 1):
				result *= num1
				num2 -= 1

			if(num2 == 0):
				result = 1
			print(result)

		if command == '8':
			print('\nCheck if a number is prime.')
			number = int(input('Enter test number: '))

			if(number == 1 or number == 2):
				print('Prime')
			#for(int i=2; i<number; i++)
			for i in range(2,number):
				if number % i == 0:
					print('Not prime')
					break
				else:
					print('Prime')
					break
		
		# NOT DONE
		if command == '9':
			print('\nFind Least Common Multiple of two numbers')
			num1 = int(input('Enter first number: '))
			num2 = int(input('Enter second number: '))
			max_poss_LCM = num1 * num2

			LCM = 2
			for i in range(2, max_poss_LCM):
				if(num1 % i == 0 and num2 % i == 0):
					LCM = i

			print(LCM)

		#Smallest multiple: smallest positive number that is evenly divisible by all numbers 1 to N
		if command == '10':
			print('\nFind smallest multiple divisible by 1 to N')
			num = int(input('Enter number: '))
			ans = 1
			for i in range(1, num+1):
				ans = (ans*i)/fractions.gcd(ans, i)
			print(ans)

		#Project euler 20: Factorial digital sum
		#find sum of digits in n!
		if command == '11':
			print('\nFind sum of digits in n!')
			num = int(input('Enter number: '))
			fact_num = math.factorial(num)
			print(str(num)+'! = ' + str(fact_num))

			sum_fact = 0
			str_num = str(num)
			str_fact_num = str(fact_num)
			for i in range(0,len(str_fact_num)):
				num_to_add = int(str_fact_num[i])
				sum_fact += num_to_add

			print('Sum of digits in ' + str_num + '! = ' + str(sum_fact))



		if command == 'q':
			print('Thank you for using the data analysis calculator.')

		else:
			print('\nUnknown command')
			command = 'reset'

		#else:
			#print('Unknown command, please try again')
			#command = 'q'
			#test_numbers = [1,5,2]
			#avg = average(test_numbers)
			#print(avg)


main()