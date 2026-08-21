import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def most_observed(birds):
    plt.xlabel('Categories')
    plt.ylabel('Count')

    count = birds['Category'].value_counts()
    count.plot(kind='bar', figsize=(12, 6))

    plt.savefig(
        'figures/observe.png',
        dpi=300,
        bbox_inches='tight'
    )


def distribution(birds):
    birds['AverageMass'] = ((birds['MinBodyMass'] + birds['MaxBodyMass']) / 2)
    birds['AverageWingspan'] = ((birds['MinWingspan'] + birds['MaxWingspan']) / 2)

    x = birds['AverageMass']
    y = birds['AverageWingspan']

    distribution2(birds)
    



def distribution2(birds):
    birds['AverageMass'].plot(kind='hist', bins=10, figsize=(12, 12))
    birds['AverageWingspan'].plot(kind='hist', bins=10, figsize=(12, 12))

    plt.savefig(
        'figures/distribution.png',
        dpi=300,
        bbox_inches='tight'
    )




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

    plt.savefig(
        'figures/distinces.png',
        dpi=300,
        bbox_inches='tight'
    )



def relation(birds):
    """
    Based on most repeated categories
    """

    counter = birds['Category'].value_counts().head(5).index
    limit = birds[birds['Category'].isin(counter)]
    
    sns.scatterplot(
        x='MinWingspan',
        y='MinBodyMass',
        hue='Category',
        data=limit
    )
    

    plt.show()


def relation2(birds):

    corr = birds[
        ["MinBodyMass",
        "MinWingspan"]
    ].corr()

    plt.figure(figsize=(10, 7))

    sns.heatmap(
        corr,
        annot=True,
        cmap='coolwarm',
        fmt='0.2f'
    )

    plt.title("Correlation Between Bird Physical Characteristics")

    plt.savefig(
        'figures/relation.png',
        dpi=300,
        bbox_inches='tight'
    )


path = 'data/birds.csv'

birds = pd.read_csv(path)


# File Checking
#print('Birds shape: \n',birds.shape)
#print('Birds head: \n',birds.head())
#print('Birds info: \n' ,birds.info())
#print('Birds unique: \n',birds.nunique())


#most_observed(birds)
#distribution(birds)
#distince(birds)
relation(birds)
#relation2(birds)

