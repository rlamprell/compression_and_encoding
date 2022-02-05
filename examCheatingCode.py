# Compute the honking protocol for the exam cheaters

def compute_and_send_code(exam):
    code = [0] * 10
    # Dont change anything above this line
    # ==========================

    from examSolutions import Encoding
    
    # choose an algorithm from the encoding class
    # -- ensure the method names match across encoding and decoding
    code = Encoding().max_actuals_largest_set(code, exam)

    # ==========================
    # Dont change anything below this line
    return code


def enter_solution_based_on_code(code):
    answer = [0] * 20

    # Dont change anything above this line
    # ==========================

    from examSolutions import Decoding

    # choose an algorithm from the dencoding class
    # -- ensure the method names match across encoding and decoding
    answer = Decoding().max_actuals_largest_set(answer, code)

    # ==========================
    # Dont change anything below this line
    return answer



