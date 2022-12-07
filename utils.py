import numpy as np
import pandas as pd 

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns 
sns.set()







def treatoutliers(df_ori, columns=None, exclusion_fraction = 0.025 , treament='cap'): 
    ## Treat Outliers using InterQuartile Ranges
    ### RobustSclaing like method

    #### Quartile method used instead of standard deviation
    #### ie: Medians instead of Means 

    #mod code = only qualtile based exclusio of a fixed number of samples 
    # right now you can do the quantile clipping  multiple times and analyse how the original and geenrated DFs are differnet
    # the above code can quite easily be modified to be memory efficient , incaseyou are maxing out your RAM, 
    #     just replace df_pri with df , remove the copy line , and the original DF will be acted upon 
    #oofcourse , eachiteration will be final , and the calculation if done again , will be done upon this modified DF , 
    # so you have only one chance to do it , but offcourse , low RAM needs
    
    df = df_ori.copy()
    #del df_ori
    
    
    
    if not columns:
        columns = df.columns
    
    for column in columns:
        treatoutliers.floor = df[column].quantile(    exclusion_fraction/2 )
        treatoutliers.ceil  = df[column].quantile(1- (exclusion_fraction/2))
        
        
        
        if treament == 'remove':
            df = df[(df[column] >= floor) & (df[column] <= ceil)]
        elif treament == 'cap':
            df[column] = df[column].clip(treatoutliers.floor, treatoutliers.ceil)
            
            df.loc[df[column] ==  np.inf , column ] = treatoutliers.ceil
            df.loc[df[column] == -np.inf , column ] = treatoutliers.floor

    return df

















def time_plots (time_level , df) :

        ax = df.groupby(time_level)['Invoice_No'].count().plot(kind='bar', figsize=(16,8))
        ax.set_xlabel(time_level,fontsize=15)
        ax.set_ylabel('Number of Orders',fontsize=15)
        ax.set_title('Orders over '+time_level ,fontsize=15)
        plt.xticks(rotation=45)
        plt.show()


        ###############


        ax = df.groupby([time_level,'Invoice_Status'])['Invoice_No'].count() \
                .unstack() [['F','C','A']].rename(columns = { 'F':'Fulfilled', 'C':'Cancelled' } ) \
                .plot.bar( stacked=True , figsize=(16,8))
                
        ax.set_xlabel(time_level,fontsize=15)
        ax.set_ylabel('Number of Orders',fontsize=15)
        ax.set_title('Orders over '+time_level+' by order status' ,fontsize=15)
        plt.xticks(rotation=45)
        plt.show()



        temp_df = df[[time_level,'Invoice_Status','Invoice_No']].astype({time_level:'str'})#.sort_values( [time_level,'Invoice_Status'] )
        temp_df['Invoice_Status'] = temp_df['Invoice_Status'].map( { 'F':'Fulfilled', 'C':'Cancelled' }  )

        # sns.set(rc = {'figure.figsize':(20,10)})
        # ax = sns.histplot(temp_df , x=time_level , hue='Invoice_Status' , multiple="stack" , discrete=True)
        # ax.set_xlabel(time_level,fontsize=15)
        # ax.set_ylabel('Number of Orders',fontsize=15)
        # ax.set_title('Orders over '+time_level+' by order status' ,fontsize=15)
        # plt.xticks(rotation=45)
        # plt.show()


        sns.set(rc = {'figure.figsize':(20,10)})
        ax = sns.histplot(temp_df , x=time_level , hue='Invoice_Status' , multiple="fill" , discrete=True)
        ax.set_xlabel(time_level,fontsize=15)
        ax.set_ylabel('Number of Orders',fontsize=15)
        ax.set_title('Orders over '+time_level+' by order status' ,fontsize=15)
        plt.xticks(rotation=45)
        plt.show()


        ###############


        ax = df.groupby([time_level,'Cust_Country_Block'])['Invoice_No'].count() \
                .unstack() [['UK', 'EUROPE', 'EIRE', 'GERM', 'FRANCE', 'OTHERS']] \
                .plot.bar( stacked=True , figsize=(16,8))
                
        ax.set_xlabel(time_level,fontsize=15)
        ax.set_ylabel('Number of Orders',fontsize=15)
        ax.set_title('Orders over '+time_level+' by Countries' ,fontsize=15)
        plt.xticks(rotation=45)
        plt.show()



        temp_df = df[[time_level,'Cust_Country_Block','Invoice_No']].astype({time_level:'str'})#.sort_values( [time_level,'Cust_Country_Block'] )

        # sns.set(rc = {'figure.figsize':(20,10)})
        # ax = sns.histplot(temp_df , x=time_level , hue='Cust_Country_Block' , multiple="stack" , discrete=True)
        # ax.set_xlabel(time_level,fontsize=15)
        # ax.set_ylabel('Number of Orders',fontsize=15)
        # ax.set_title('Orders over '+time_level+' by Countries' ,fontsize=15)
        # plt.xticks(rotation=45)
        # plt.show()


        sns.set(rc = {'figure.figsize':(20,10)})
        ax = sns.histplot(temp_df , x=time_level , hue='Cust_Country_Block' , multiple="fill" , discrete=True , color = 'Pastel1')
        ax.set_xlabel(time_level,fontsize=15)
        ax.set_ylabel('Number of Orders',fontsize=15)
        ax.set_title('Orders over '+time_level+' by Countries' ,fontsize=15)
        plt.xticks(rotation=45)
        plt.show()


        ###############


        # ax = df.groupby([time_level,'Misc_Product_Code_Flag'])['Invoice_No'].count() \
        #         .unstack() \
        #         .plot.bar( stacked=True , figsize=(16,8))
                
        # ax.set_xlabel(time_level,fontsize=15)
        # ax.set_ylabel('Number of Orders',fontsize=15)
        # ax.set_title('Orders over '+time_level+' by Special Trns' ,fontsize=15)
        # plt.show()



        # temp_df = df[[time_level,'Misc_Product_Code_Flag','Invoice_No']].astype({time_level:'str'})#.sort_values( [time_level,'Invoice_Status'] )

        # sns.set(rc = {'figure.figsize':(20,10)})
        # ax = sns.histplot(temp_df , x=time_level , hue='Misc_Product_Code_Flag' , multiple="stack" , discrete=True)
        # ax.set_xlabel(time_level,fontsize=15)
        # ax.set_ylabel('Number of Orders',fontsize=15)
        # ax.set_title('Orders over '+time_level+' by Special Trns' ,fontsize=15)
        # plt.xticks(rotation=45)
        # plt.show()


        # sns.set(rc = {'figure.figsize':(20,10)})
        # ax = sns.histplot(temp_df , x=time_level , hue='Misc_Product_Code_Flag' , multiple="fill" , discrete=True , color = 'Pastel1')
        # ax.set_xlabel(time_level,fontsize=15)
        # ax.set_ylabel('Number of Orders',fontsize=15)
        # ax.set_title('Orders over '+time_level+' by Special Trns' ,fontsize=15)
        # plt.xticks(rotation=45)
        # plt.show()
