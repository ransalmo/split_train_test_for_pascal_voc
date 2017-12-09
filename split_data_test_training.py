#splits data into test and training sets
import os
import math
import random
import shutil

def main():
    print('Split test and training sets')
    image_path = os.path.join(os.getcwd())
    annotations_path = os.path.join(image_path,'annotations')
    imageArr = [x for x in os.listdir(image_path) if x.endswith('.jpg')]
    #shuffle array
    random.shuffle(imageArr)
    percentageTrain = 0.9
    trainFileNumber = int(len(imageArr) * percentageTrain)
    testFileNumber = len(imageArr) - trainFileNumber
    trainingBasePath = os.path.join(image_path, 'training')
    testBasePath = os.path.join(image_path,'test')
    #check and create foldes if neceasary
    if not os.path.exists(trainingBasePath):
        os.makedirs(trainingBasePath)
    if not os.path.exists(testBasePath):
        os.makedirs(testBasePath)
    if not os.path.exists(os.path.join(trainingBasePath,'csv')):
        os.makedirs(os.path.join(trainingBasePath,'csv'))
    if not os.path.exists(os.path.join(image_path, 'training','annotations')):
        os.makedirs(os.path.join(image_path, 'training','annotations'))
    if not os.path.exists(os.path.join(image_path, 'test')):
        os.makedirs(os.path.join(image_path, 'test'))
    if not os.path.exists(os.path.join(image_path, 'test', 'csv')):
        os.makedirs(os.path.join(image_path, 'test', 'csv'))
    if not os.path.exists(os.path.join(image_path, 'test', 'annotations')):
        os.makedirs(os.path.join(image_path, 'test', 'annotations'))
    currentCopyPath = ''
    for index, fileName in enumerate(imageArr):
        if (index+1) < trainFileNumber:
            currentCopyPath = trainingBasePath
        else:
            currentCopyPath = testBasePath
        ##copy image
        shutil.copy(os.path.join(image_path, fileName), currentCopyPath)
        ##copy annotations
        annotationsFile = fileName.replace('jpg','xml')
        shutil.copy(os.path.join(image_path, 'annotations', annotationsFile), os.path.join(currentCopyPath, 'annotations'))

main()
