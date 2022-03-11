import pandas as pd
import glob
import numpy as np
import scipy as sp
import scipy.stats


#------------------------------------------------------------------------------------
def TXT2CSV(file):
    # print(file)
    f = open(file, 'r')
    data = []
    equation = []
    flag = False

    for index, line in enumerate(f.readlines()):
        if index == 0:
            mts_var = line.split()
            data.append(line.split())
        elif index == 1:
            name = line.split()
        else:
            line = line.strip('\n')
            if line == '' or line == 'equation':
                flag = True
            elif flag == True:
                equation.append(line)
            else:
                data.append(line.split())

    df = pd.DataFrame(data, columns=name)
    f.close

    return df, equation


#------------------------------------------------------------------------------------
def TXT2CSV_ALL(path):
    path = path + '/*.txt'
    files = glob.glob(path)

    for file in files:
        # print(file)
        f = open(file, 'r')
        csv_file = file.replace('.txt', '.csv')
        eq_file = file.replace('.txt', '.eq')
        # print(csv_file)
        data = []
        equation = []
        flag = False

        for index, line in enumerate(f.readlines()):
            if index == 0:
                mts_var = line.split()
                data.append(line.split())
            elif index == 1:
                name = line.split()
            else:
                line = line.strip('\n')
                if line == '' or line == 'equation':
                    flag = True
                elif flag == True:
                    equation.append(line)
                else:
                    data.append(line.split())

        df = pd.DataFrame(data, columns=name)
        df.to_csv(csv_file)
        # print(equation)
        with open(eq_file,'w',encoding='UTF-8') as f:
            for eq in equation:
                f.write(eq + '\n')
        f.close



#------------------------------------------------------------------------------------
def VarList(df):
    column = df.columns.to_list()
    vlist = df.loc[0].to_list()
    varlist = []
    mtslist = []

    for index, list in enumerate(vlist):
        # print(list, index, column[index])
        # if list[0] == 'M':
        #     mtslist.append(column[index])
        # elif list[0]  == 'V':
        #     varlist.append(column[index])
        if list == 'V1':
            varstart = index
    df = df.drop(0, axis=0)
    # print(df)

    return df, column, varstart
    # return mtslist, varlist, df



#------------------------------------------------------------------------------------

def SplitEquation(list):
    eq = list.find('=')
    result = list[:eq].strip()
    body = list[eq + 1:].strip()

    return result, body


#------------------------------------------------------------------------------------
def Change2NUMPY(str):
    str = str.replace('tan', 'np.tan')
    str = str.replace('sin', 'np.sin')
    str = str.replace('cos', 'np.cos')

    return str


#------------------------------------------------------------------------------------
def ExtractFileName(name):
    filename = name[name.rfind('\\') + 1:]
    filename = filename[:filename.find('.')]

    return filename

#------------------------------------------------------------------------------------
def AnalMargin(df_cases, sampleNum):
    df_result_line = []
    dfout = df_cases['Output']
    # print(dfout)

    df_result_column = ['min', 'max', 'mean', 'var', 'std', '1s', '2s', '3s', '4.5s']
    # result_column = ['min', 'max', 'mean', 'var', 'std', '1s', '1sN', '2s', '2sN', '3s', '3sN', '4.5s', '4.5sN']
    # print(result_column)
    # print(dfout.min(), dfout.max(), dfout.mean(), dfout.var(), dfout.std())
    df_result_line.append(round(dfout.min(),2))
    df_result_line.append(round(dfout.max(),2))
    df_result_line.append(round(dfout.mean(),2))
    df_result_line.append(round(dfout.var(),2))
    df_result_line.append(round(dfout.std(),2))
    std = dfout.std()

    # sigmalist = [-1]
    sigmalist = [-1, -2, -3, -4.5]
    xx = np.linspace(-8, 8, 100)
    rv_norm = sp.stats.norm(loc=0, scale=1)
    rv = sp.stats.norm(loc=dfout.mean(), scale=dfout.std())

    for sigma in sigmalist:
        cdf_normal = rv_norm.cdf(sigma)
        index = int(sampleNum * cdf_normal)
        df_result_line.append(round(dfout[index], 2))
        # ppf_value = round(rv.ppf(cdf_normal), 2)
        # df_result.append(ppf_value)
        # print(std, sampleNum, index, round(dfout[index], 2), ppf_value)

    # print(df_result)
    return df_result_column, df_result_line



# path = 'D:\Python\Margin\data'
# TXT2CSV_ALL(path)

# list = 'Output = Min(0, S2)'
# result, body = SplitEquation(list)
# print(result, body)