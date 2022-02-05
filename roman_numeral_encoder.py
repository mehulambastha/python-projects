# -----------------------------------------------------------------------------------
# MADE BY: mehul ambastha [@mehulambastha on codewars, and @mehul.ambastha on github]
# -----------------------------------------------------------------------------------


def solution(n):
    # a dictionary to store the values. Here to avoid using four consecutive numeral for a number (like XXXX for 40, it has been given its own numeral separately. similarly for 90 and 900 and 400 etc.)
    roman = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    # convert the given number into string to use string methods and split it.
    n_str = str(n)
    # the answer
    answer = ''

    print(f"length of the given number is {len(n_str)}")
    # a loop to interate over the number and break it into sub=parts: thousandths, hundredths, tens, onces and so on
    # 'enumerate' to get a counter along with iteration
    for index, x in enumerate(list(n_str)):
        print(f"index is {index} and digit is {x}")

        # most important line of code. It separates the number to thousandths, hundredths, or tens place
        # add zeroes in front of the split separate digits.(eg: if original number is 1576, it converts that into 1000 in first iteration, then 500 in 2nd iteration, then 70 in 3rd, and finally 6 in last iteration)
        num = str(x) + "0"*(len(n_str) - index - 1)

        print(
            f"Current value of num is {int(num)} (int value) . and {num} (str value)")

        # matching and finding corresponding alphabet from the dictionary
        if int(num) in roman:
            # if it is directly found in the dictionary.
            answer += roman[int(num)]
        else:
            # --------------------------------------------------------------------------------
            # WORKS ON THE BASIS OF SUBTRACTING THE NUMBERS DESIGNATED TO VARIOUS ALPHABETS IN ROMAN NUMERAL. ie, IT FINDS ANSWERS BY RECURSIVELY SUBTRACTING NUMBERS LESS THAN THE argument UNTIL THE ANSWER IS OBTAINED
            # --------------------------------------------------------------------------------

            # if the number is not directly available in dict.
            # length of the current split number (eg: 30 ,70, 100, 200)
            l = len(num)

            # a list of the keys from dictionary.
            keys = list(roman.keys())

            # possible answers (in alphabet) less than the length of current num (eg: if its 30 then returns 10, if its 600 returns 100, 400, 500 etc)
            # this list contains alphabets and not actual numbers to subtract.
            near_ans = [roman[key] for key in keys if key < int(num)]

            # contains actual numbers to subtract corresponding to the roman numerals selected above.
            keys_to_subtract = [
                list(roman.keys())[list(roman.values()).index(ans)] for ans in near_ans]

            # sort the numbers obtained above in reverse order so as to subract the greatest number first
            keys_to_subtract.sort(reverse=True)

            # converted into int type for arithmetic operations
            int_num = int(num)

            # iterating over the numbers to subtract, with greatest number first.
            for n in keys_to_subtract:
                # only if the number is greater  > 0 {ie, answer hasn't been found yet. bcz answer is found when the number reduces to zero on repeated subtraction}
                if int_num > 0:
                    print(
                        f"current n is {n}.")

                    # while the current split number (eg: 1000, 700, etc) is greater than or equal to the 'number' from keys of {roman} dict.
                    while int_num >= n:
                        print(f"\t{int_num} is greater than {n}")
                        print(
                            f"\t::subtracting {n} from {int_num}, int_num remaining is {int_num - n}")

                        # subtract the 'n' from the current split number
                        # eventually, the int_num will become zero. At that point answer would have been found.
                        int_num -= n
                        # add the alphabet corresponding to the number which was subtracted above.
                        answer += roman.get(n)
                        # for confirmation
                        print(f"\t->added {roman.get(n)} to the answer")
                else:
                    break  # break the loop if answer has been found

            print(answer, " for {} \n ----------------------------------------------------------------------------".format(num))

    print(f"Final answer: {answer}")
    return answer


solution(674)
