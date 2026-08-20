import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def most_observed(birds):
    plt.xlabel('Categories')
    plt.ylabel('Count')

    count = birds['Category'].value_counts()
    count.plot(kind='bar', figsize=(12, 6))

    plt.show()


def frequently(birds):
    birds['AverageMass'] = ((birds['MinBodyMass'] + birds['MaxBodyMass']) / 2)
    birds['AverageWingspan'] = ((birds['MinWingspan'] + birds['MaxWingspan']) / 2)

    x = birds['AverageMass']
    y = birds['AverageWingspan']

    frequently2(birds)
    



def frequently2(birds):
    birds['AverageMass'].plot(kind='hist', bins=10, figsize=(12, 12))
    birds['AverageWingspan'].plot(kind='hist', bins=10, figsize=(12, 12))

    plt.show()




def distince(birds):
    D1 = birds.groupby('Category')[['MinBodyMass', 'MaxBodyMass']].mean()
    D2 = birds.groupby('Category')[['MinWingspan', 'MaxWingspan']].mean()


    D1.plot(
        kind='bar',
        figsize=(12, 12)
    )


    D2.plot(
        kind='bar',
        figsize=(12, 12)
    )




    plt.title('Physical Characteristics by Bird Category')
    plt.suptitle('')
    plt.xlabel('Category')
    plt.ylabel('Average Value')
    plt.tight_layout()

    plt.show()




path = 'data/birds.csv'

birds = pd.read_csv(path)


# File Checking
#print('Birds shape: \n',birds.shape)
#print('Birds head: \n',birds.head())
#print('Birds info: \n' ,birds.info())
#print('Birds unique: \n',birds.nunique())


#most_observed(birds)
#frequently(birds)
distince(birds)

