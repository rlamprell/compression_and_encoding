# This file includes the Encoding and Decoding methods for Assignment 2 - Exam Codes.
#
# The methods have been seperated by classes as to ensure there is no cross-talk
# between the declared variables.
# 
# When Encoding and Decoding, please ensure to use the same method name under both
# classes, example:  Encoding().simple() -> Decoding.simple()
#
# Last Modified:    2021/05/09
#                   Rob Lamprell 


# Encode the exam solutions
class Encoding:
    
    # simple one-to-one mapping of 10 answers
    def simple(self, code, exam):
        
        for i in range(len(code)):
            code[i] = exam[i]

        return code


    # groupings of three
    # -- example [1, 0] -> [1]
    def sets_of_two(self, code, exam):
        
        for i in range(len(code)):

            # to iterate it would be 2i, 2i+1
            # -- if the count is greater than 0 then the dominate 
            #    feature is 1 and not 0.
            count = exam[2*i] + exam[2*i+1]
            if count > 0:
                code[i] = 1
            else:
                code[i] = 0

        return code


    # groupings of three
    # -- example [1, 0, 1] -> [1]
    def sets_of_three(self, code, exam):
        
        for i in range(len(code)):

            # stop when we reach the end of the 20 questions
            if 3*i+2 > 19:
                break

            # to iterate it would be 3i, 3i+1, 3i+2
            # -- if the count is greater than 1 then the dominate 
            #    feature is 1 and not 0.
            count = exam[3*i] + exam[3*i+1] + exam[3*i+2]
            if count > 1:
                code[i] = 1
            else:
                code[i] = 0

        return code


    # five groupings of three and the rest filled
    # with one-to-one mappings
    # -- example    [1, 0, 1] -> [1]
    #               [1, 0, 0] -> [0]
    #               [1, 0, 1] -> [1]
    #               ...
    #               [0]       -> [0]
    #               ...
    #               [1]       -> [1]
    def sets_of_5threes_fill(self, code, exam):
        
        for i in range(len(code)):

            # stop when we reach the 5 groups of three
            if 3*i+2 > 14:
                break

            # to iterate it would be 3i, 3i+1, 3i+2
            # -- if the count is greater than 1 then the dominate 
            #    feature is 1 and not 0.
            count = exam[3*i] + exam[3*i+1] + exam[3*i+2]
            if count > 1:
                code[i] = 1
            else:
                code[i] = 0

        # 5 one-to-one mappings
        for i in range(5, 10):
            code[i] = exam[i+10]

        return code


    # groupings of five
    # -- example    [1, 0, 1, 0, 1] -> [1]
    #               [1, 0, 1, 0, 1] -> [1]
    #               [1, 0, 1, 0, 1] -> [1]
    #               [1, 0, 1, 0, 1] -> [1]
    def sets_of_five(self, code, exam):

        for i in range(len(code)):

            # stop when we reach the end of the 20 questions
            if 5*i+4 > 19:
                break

            # to iterate it would be 3i, 3i+1, 3i+2
            # -- if the count is greater than 1 then the dominate 
            #    feature is 1 and not 0.
            count = exam[5*i] + exam[5*i+1] + exam[5*i+2] + exam[5*i+3] + exam[5*i+4]
            if count > 2:
                code[i] = 1
            else:
                code[i] = 0

        return code


    # two groupings of five, one of three and the rest filled
    # with one-to-one mappings
    # -- example    [1, 0, 1, 0, 1] -> [1]
    #               [1, 0, 1, 0, 1] -> [1]
    #               [1, 0, 1]       -> [1]
    #               [0]             -> [0]
    #               ...
    #               [1]             -> [1]
    def sets_of_2fives_1three_fill(self, code, exam):
        
        for i in range(len(code)):

            # stop when we reach 2 groups of five
            if 5*i+4 > 9:
                break

            # to iterate it would be 3i, 3i+1, 3i+2
            # -- if the count is greater than 1 then the dominate 
            #    feature is 1 and not 0.
            count = exam[5*i] + exam[5*i+1] + exam[5*i+2] + exam[5*i+3] + exam[5*i+4]
            if count > 2:
                code[i] = 1
            else:
                code[i] = 0
        
        # 1 group of three
        for i in range(2, 3):
            count = exam[10] + exam[11] + exam[12]

            if count > 1:
                code[i] = 1
            else:
                code[i] = 0

        # 7 one-to-one mappings
        for i in range(3, 10):
            code[i] = exam[i+10]

        return code


    # use as many actual results as possible and 
    # take the majority from the remaining set
    # n-1 one-to-one mappings and max single grouping
    def max_actuals_largest_set(self, code, exam):

        # one less than the code length
        actual = len(code)-1

        # for every code value (except the final)
        # make the code the same value as the exam
        for i in range(actual):
            code[i] = exam[i]

        # count the number of 1s in the remaining exam indexes
        count = 0
        for i in range(actual, len(exam)):
            count += exam[i]

        # if 1 is in the majority then code[len] = 1
        # else it must be 0
        RHS_subset = len(exam) - actual
        if count >= (RHS_subset/2):
            code[actual] = 1
        else:
            code[actual] = 0

        return code




# Decode the exam solutions
class Decoding:

    # simple one-to-one mapping of 10 answers
    def simple(self, answer, code):
        
        for i in range(len(code)):
            answer[i] = code[i]

        return answer


    # groupings of three
    # -- example [1] -> [1, 1]
    def sets_of_two(self, answer, code):
        
        # decode in sets of three
        for i in range(len(code)):

            answer[2*i]     = code[i]
            answer[2*i+1]   = code[i]

        return answer


    # groupings of three
    # -- example [1] -> [1, 1, 1]
    def sets_of_three(self, answer, code):
        
        # decode in sets of three
        for i in range(len(code)):

            # stop when we reach the end of the 20 questions
            if 3*i+2 > 19:
                break

            answer[3*i]     = code[i]
            answer[3*i+1]   = code[i]
            answer[3*i+2]   = code[i]

        return answer


    # five groupings of three and the rest filled
    # with one-to-one mappings
    # -- example    [1] -> [1, 1, 1]
    #               [1] -> [0, 0, 0]
    #               [1] -> [1, 1, 1]
    #               ...
    #               [0] -> [0]
    #               ...
    #               [1] -> [1]
    def sets_of_5threes_fill(self, answer, code):
        
        # decode in sets of three
        for i in range(len(code)):

            # ensure the five groupings is not exceeded
            if 3*i+2 > 14:
                break
            
            answer[3*i]     = code[i]
            answer[3*i+1]   = code[i]
            answer[3*i+2]   = code[i]

        # 5 one-to-one mappings
        for i in range(5, 10):
            answer[i+10] = code[i]

        return answer


    # groupings of five
    # -- example    [1] -> [1, 1, 1, 1, 1]
    #               [0] -> [0, 0, 0, 0, 0]
    #               [1] -> [1, 1, 1, 1, 1]
    #               [1] -> [1, 1, 1, 1, 1]
    def sets_of_five(self, answer, code):

        # decode into 4 groups of five
        for i in range(len(code)):

            # stop when we reach the end of the 20 questions
            if 5*i+4 > 19:
                break

            answer[5*i]     = code[i]
            answer[5*i+1]   = code[i]
            answer[5*i+2]   = code[i]
            answer[5*i+3]   = code[i]
            answer[5*i+4]   = code[i]

        return answer


    # two groupings of five, one of three and the rest filled
    # with one-to-one mappings
    # -- example    [1] -> [1, 1, 1, 1, 1]
    #               [1] -> [1, 1, 1, 1, 1]
    #               [1] -> [1, 1, 1]
    #               [0] -> [0]
    #               ...
    #               [1] -> [1]
    def sets_of_2fives_1three_fill(self, answer, code):

        # decode 2 groups of five
        for i in range(len(code)):

            # stop after the two decodings
            if 5*i+4 > 9:
                break

            answer[5*i]     = code[i]
            answer[5*i+1]   = code[i]
            answer[5*i+2]   = code[i]
            answer[5*i+3]   = code[i]
            answer[5*i+4]   = code[i]

        # decode 1 group of three
        answer[10]   = code[i]
        answer[11]   = code[i]
        answer[12]   = code[i]

        # 7 one-to-one mappings
        for i in range(3, 10):

            answer[i+10] = code[i]

        return answer


    # use as many actual results as possible and 
    # take the majority from the remaining set
    # n-1 one-to-one mappings and max single grouping
    def max_actuals_largest_set(self, answer, code):

        # n-1
        actual = len(code)-1

        # nine one-to-one mappings
        for i in range(actual):
            answer[i] = code[i]

        # use the 1 eleven grouping to populate the rest
        for i in range(actual, len(answer)):
            answer[i] = code[actual]

        return answer