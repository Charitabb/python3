import numpy as np

def MSE(pred, target):
    pred = np.array(pred)
    target = np.array(target)
    assert pred.shape == target.shape, 'array need to be the same shape'
    n = pred.size
    x = (np.array(pred) - np.array(target)) **2
    return x.sum()/n

def MSE_2d(pred, target):
    pred = np.array(pred)
    target = np.array(target)
    assert pred.shape == target.shape, 'array need to be the same shape'
    n = len(pred)
    x = (pred - target) **2
    return x.sum(axis=1)/n

def MAE(pred, target):
    pred = np.array(pred)
    target = np.array(target)
    assert pred.shape == target.shape, 'array need to be the same shape'
    n = pred.size
    x = np.array(pred) - np.array(target)
    x = np.abs(x)
    return x.sum()/n

def MAE_2d(pred, target):
    pred = np.array(pred)
    target = np.array(target)
    assert pred.shape == target.shape, 'array need to be the same shape'
    n = len(pred)
    x = abs(pred - target)
    return x.sum(axis=1)/n

def accuracy(pred, target):
    pred = np.array(pred)
    target = np.array(target)
    assert pred.shape == target.shape, 'array need to be the same shape'
    n = pred.size
    return np.sum(pred == target) /n

def accuracy_2d(pred,target):
    pred = np.array(pred)
    target = np.array(target)
    assert pred.shape == target.shape, 'array need to be the same shape'
    n = pred.size / len(pred)
    x = (pred == target)
    return x.sum(axis=1)/n
    

def exam():
    x = input()
    list = []
    list2 = []
    list3 =[]

    while x != '0':
        y = x.split()
        list.append(y)

        x = input()
        user = np.array(list)


    ans = input().split()
    list2.append(ans)
    a = np.array(list2)

    score = input().split()
    list3.append(score)
    score = np.array(score)

    result = []

    for i in range(len(user)):
        for j in range(len(ans)):
            if user[i,j] == ans[j]:
                result.append(int(score[j]))
            else:
                result.append(0)

    result = np.array(result)
    result = result.reshape(len(user), len(ans))
    print(result.sum(axis=1))




print(MSE([5,9], [3,4]))
print(MSE_2d(([5,9], [8,1]), ([3,4], [2,6])))
print(MSE_2d(([2,8], [7,3]), ([7,9], [8,3])))
print(MAE_2d(([[5,9], [8,1]]), ([[3,4], [2,6]])))
print(MAE_2d(([2,8], [7,3]), ([7,9], [8,3])))
print(accuracy([1,0,0,1], [1,0,1,1]))
print(accuracy_2d(([[1,0,0,1], [0,1,0,1]]), ([[1,1,1,1], [1,0,0,1]])))
print(accuracy_2d(([[0,1,1,1], [1,1,1,0]]), ([[0,1,0,1], [0,1,0,1]])))