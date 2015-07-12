class Question2_Solver:
    def __init__(self):
        self.learn('train.data');
        return;

    # Add your code here.
    # Read training data and build your naive bayes classifier
    # Store the classifier in this class
    # This function runs only once when initializing
    # Please read and only read train_data: 'train.data'
    def learn(self, train_data):
        with open(train_data, "r") as f:
            data = f.read().splitlines();
        temp1 = list()
        temp2 = list()
        dtemp_l = list()
        dtemp_d = list()
        rtemp_l = list()
        rtemp_d = list()
        count = 0
        for row in data:
            instance = row.split();
            s = ""
            temp_count = 0
            for i in instance[1]:
                if i != ",":
                    s = s + i
                    temp_count = temp_count+1
            count = temp_count
            temp1.append(instance[0])
            temp2.append(s)
        total = 0
        count_d = 0
        count_r = 0
        alpha = 0.0001
        
        count_y = [0 for i in range(count)]
        count_n = [0 for i in range(count)]
        count_a = [0 for i in range(count)]
        
        #get the total number of data and the number of democrat and the number of republican
        for row in range(len(temp2)):
            if temp1[row] == "democrat":
                total = total+1
                count_d = count_d+1
                dtemp_l.append(temp1[row])
                dtemp_d.append(temp2[row])
            else:
                total = total+1
                count_r = count_r+1
                rtemp_l.append(temp1[row])
                rtemp_d.append(temp2[row])
            
            for col in range(count):
                if temp2[row][col] == "y":
                    count_y[col] = count_y[col]+1
                elif temp2[row][col] == "n":
                    count_n[col] = count_n[col]+1
                else:
                    count_a[col] = count_a[col]+1
            

        dcount_y = [0 for i in range(count)]
        dcount_n = [0 for i in range(count)]
        dcount_a = [0 for i in range(count)]
        rcount_y = [0 for i in range(count)]
        rcount_n = [0 for i in range(count)]
        rcount_a = [0 for i in range(count)]
        for col in range(count):
            for row in range(len(dtemp_d)):
                if dtemp_d[row][col] == "y":
                    dcount_y[col] = dcount_y[col]+1
                elif dtemp_d[row][col] == "n":
                    dcount_n[col] = dcount_n[col]+1
                else:
                    dcount_a[col] = dcount_a[col]+1
            for row in range(len(rtemp_d)):
                if rtemp_d[row][col] == "y":
                    rcount_y[col] = rcount_y[col]+1
                elif rtemp_d[row][col] == "n":
                    rcount_n[col] = rcount_n[col]+1
                else:
                    rcount_a[col] = rcount_a[col]+1

        #get the probility of every feature when feature equal possible values under the republican or democrat with or without smoothing method
        for i in range(count):
            """
            dcount_y[i] = (1.0*(dcount_y[i]+alpha*count_y[i]))/(count_d+alpha*total)
            dcount_n[i] = (1.0*(dcount_n[i]+alpha*count_n[i]))/(count_d+alpha*total)
            dcount_a[i] = (1.0*(dcount_a[i]+alpha*count_a[i]))/(count_d+alpha*total)
            rcount_y[i] = (1.0*(rcount_y[i]+alpha*count_y[i]))/(count_r+alpha*total)
            rcount_n[i] = (1.0*(rcount_n[i]+alpha*count_n[i]))/(count_r+alpha*total)
            rcount_a[i] = (1.0*(rcount_a[i]+alpha*count_a[i]))/(count_r+alpha*total)
            """
            dcount_y[i] = (1.0*dcount_y[i])/count_d
            dcount_n[i] = (1.0*dcount_n[i])/count_d
            dcount_a[i] = (1.0*dcount_a[i])/count_d
            rcount_y[i] = (1.0*rcount_y[i])/count_r
            rcount_n[i] = (1.0*rcount_n[i])/count_r
            rcount_a[i] = (1.0*rcount_a[i])/count_r
            
        d_prior = (1.0*count_d)/total
        r_prior = (1.0*count_r)/total
        self.d_prior = d_prior
        self.r_prior = r_prior
        self.dcount_y = dcount_y
        self.dcount_n = dcount_n
        self.dcount_a = dcount_a
        self.rcount_y = rcount_y
        self.rcount_n = rcount_n
        self.rcount_a = rcount_a
        return;

    # Add your code here.
    # Use the learned naive bayes classifier to predict
    # query example: 'n,y,n,y,y,y,n,n,n,y,?,y,y,y,n,y'
    # return 'republican' or 'republican'
    def solve(self, query):
        string = ""
        for i in query:
            if i != ",":
                string = string+i
        d_prob = self.d_prior
        r_prob = self.r_prior
        for i in range(len(string)):
            if string[i] == "y":
                d_prob = d_prob*self.dcount_y[i]
                r_prob = r_prob*self.rcount_y[i]
            elif string[i] == "n":
                d_prob = d_prob*self.dcount_n[i]
                r_prob = r_prob*self.rcount_n[i]
            else:
                d_prob = d_prob*self.dcount_a[i]
                r_prob = r_prob*self.rcount_a[i]
        if d_prob > r_prob:
            return 'democrat'
        elif d_prob == r_prob:
            return 'democrat'
        else:
            return 'republican'

