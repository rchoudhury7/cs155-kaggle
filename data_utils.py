import numpy as np
from sklearn.preprocessing import StandardScaler

def load(filename, test=False, normalize=True):
    f = open(filename, 'rb')
    data = np.loadtxt(f, dtype='float', delimiter=',', skiprows=1)
    f.close()
    
    if test:
        # ignore first column of ids
        X = data[:, 1:]
        # normalize
        if normalize:
            X = StandardScaler().fit_transform(X)
        return X
    else:
        X,y = data[:, 1:-1], data[:, -1]
        # normalize
        if normalize:
            X = StandardScaler().fit_transform(X)
        y = y.astype('int')
        return X,y
    

def load_train(filename, normalize=True):
    X, y = load(filename, False, normalize)
    return X, y


def load_test(filename, normalize=True):
    X = load(filename, True, normalize)
    return X


def write_test(filename, preds):
    f = open(filename, 'w')
    
    f.write("Id,PES1\n")
    for i in xrange(len(preds)):
        f.write('%s,%d\n' %(str(i), int(preds[i])))
    
    f.close()


if __name__=='__main__':
    train = './data/train_2008.csv'
    
    X, y = load_train(train)
    print 'X: ', X.shape
    print 'y: ', y.shape
    
    print X[0], y[0]
