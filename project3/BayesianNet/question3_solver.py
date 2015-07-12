class Question3_Solver:
    def __init__(self, cpt):
        self.cpt = cpt;
        self.creat_cpt_1_hidden();
        self.creat_cpt_2_hidden();

    #####################################
    # ADD YOUR CODE HERE
    # Pr(x|y) = self.cpt.conditional_prob(x, y);
    # A word begins with "`" and ends with "`".
    # For example, the probability of word "ab":
    # Pr("ab") = \
    #    self.cpt.conditional_prob("a", "`") * \
    #    self.cpt.conditional_prob("b", "a") * \
    #    self.cpt.conditional_prob("`", "b");
    # query example:
    #    query: "qu--_--n";
    #    return "t";

    def creat_cpt_1_hidden(self):#precompute the cpt1 which has one hidden letter
        ch = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.cpt1 = [[0.0] * 27 for i in range(27)]
        for i in range(0, 27):
            for j in range(0, 27):
                for k in ch:
                    if i == 0 and j != 0:
                        self.cpt1[i][j] = self.cpt1[i][j] + self.cpt.conditional_prob(k,'`')*self.cpt.conditional_prob(chr(96+j),k)
                    elif i != 0 and j == 0:
                        self.cpt1[i][j] = self.cpt1[i][j] + self.cpt.conditional_prob(k,chr(96+i))*self.cpt.conditional_prob('`',k)
                    elif i == 0 and j == 0:
                        continue
                    else:
                        self.cpt1[i][j] = self.cpt1[i][j] + self.cpt.conditional_prob(k,chr(96+i))*self.cpt.conditional_prob(chr(96+j),k)
        
    def conditional_prob_1_hidden(self, v, given):
        return self.cpt1[ord(given) - 96][ord(v) - 96];

    def creat_cpt_2_hidden(self):#precompute the cpt2 which has two hidden letters
        self.cpt2 = [[0.0] * 27 for i in range(27)]
        for i in range(0,27):
            for j in range(0,27):
                for k in range(1,27):
                    if i != 0 and j == 0:
                        self.cpt2[i][j] = self.cpt2[i][j] + self.cpt1[i][k]*self.cpt.conditional_prob('`',chr(96+k))
                    elif i == 0 and j == 0:
                        continue
                    else:
                        self.cpt2[i][j] = self.cpt2[i][j] + self.cpt1[i][k]*self.cpt.conditional_prob(chr(96+j),chr(96+k))

    def conditional_prob_2_hidden(self, v, given):
        return self.cpt2[ord(given) - 96][ord(v) - 96];


    def solve(self, query):
        letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        
        position = 0
        for i in range(len(query)):
            max_p = 0
            max_position = 0
            if query[i] == "_":
                if i == 0:
                    for j in range(len(letter)):
                        possible = self.cpt.conditional_prob(letter[j], "`")*self.conditional_prob_2_hidden(query[i+3], letter[j])
                        if max_p < possible:
                            max_p = possible
                            max_position = j
                    position = max_position
                    break
                elif i == 1:
                    for j in range(len(letter)):
                        possible = self.conditional_prob_1_hidden(letter[j], "`")*self.conditional_prob_2_hidden(query[i+3], letter[j])
                        if max_p < possible:
                            max_p = possible
                            max_position = j
                    position = max_position
                    break
                elif i == 2:
                    for j in range(len(letter)):
                        possible = self.conditional_prob_2_hidden(letter[j], "`")*self.conditional_prob_2_hidden(query[i+3], letter[j])
                        if max_p < possible:
                            max_p = possible
                            max_position = j
                    position = max_position
                    break
                elif i == len(query)-1:
                    for j in range(len(letter)):
                        possible = self.conditional_prob_2_hidden(letter[j], query[i-3])*self.cpt.conditional_prob("`", letter[j])
                        if max_p < possible:
                            max_p = possible
                            max_position = j
                    position = max_position
                    break
                elif i == len(query)-2:
                    for j in range(len(letter)):
                        possible = self.conditional_prob_2_hidden(letter[j], query[i-3])*self.conditional_prob_1_hidden("`", letter[j])
                        if max_p < possible:
                            max_p = possible
                            max_position = j
                    position = max_position
                    break
                elif i == len(query)-3:
                    for j in range(len(letter)):
                        possible = self.conditional_prob_2_hidden(letter[j], query[i-3])*self.conditional_prob_2_hidden("`", letter[j])
                        if max_p < possible:
                            max_p = possible
                            max_position = j
                    position = max_position
                    break
                else:
                    for j in range(len(letter)):
                        possible = self.conditional_prob_2_hidden(letter[j], query[i-3])*self.conditional_prob_2_hidden(query[i+3], letter[j])
                        if max_p < possible:
                            max_p = possible
                            max_position = j
                    position = max_position
                    break


        return letter[position];
        
        
        

        

