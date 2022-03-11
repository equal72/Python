import pandas as pd
from Functions import *
from distance import *
from drawgraph import *
import glob
import numpy as np



path = 'C:\Python\Projects\margin_cvs\data'
infile = path + '/*.txt'
files = glob.glob(infile)

for file in files:
    filename = ExtractFileName(file)
    df = pd.DataFrame()
    equation = []
    column = []
    anal_column = []
    df_anal_file = ''
    case = ''
    result = ''
    body = ''
    varstart = 0
    PI = np.pi
    sampleNum = 100


    df, equations = TXT2CSV(file)
    df, column, varstart = VarList(df)
    newcolumn = column
    newcolumn.append('Output')
    # print(df)
    # print(newcolumn)
    # print(varstart)
    # print(column)
    # print(column[:varstart])
    # print(column[varstart:])
    # print(equations)
    eqlist = ['Ax = CPP/2-VA_TCD/2+H_VA*2', 'Ay = tan(PI*VA_slope/180)', 'output = VA_CDU + VA_PC_OVL']

    for indexrow, row in df.iterrows():
        df_case = pd.DataFrame(columns=newcolumn)
        df_case_file = ''
        for i in range(sampleNum):
            newcase = []
            for idx, value in enumerate(row):
                value = float(row[idx])
                if idx >= varstart:
                    value = round(np.random.randint(0, 100)/100 * value * 2 - value, 2)
                elif idx < varstart:
                    value = round(value, 2)
                newcase.append(value)
                globals()[column[idx]] = round(value, 2)
            # newcase = row.to_list()

            for eq in equations:
                result, body = SplitEquation(eq)
                # print(result, body)
                body = Change2NUMPY(body)
                globals()[result] = round(eval(body), 2)
            newcase.append(Output)
            df_case.loc[i] = newcase

        # print(df_case)
        df_case = df_case.sort_values(by=df_case.columns[len(df.columns) - 1], ignore_index=True)
        df_case_file = path + '\\' + filename + '_' + str(indexrow) + '.csv'
        df_case.to_csv(df_case_file)
        DrawHisto(df_case)
        print(f'Margin list file \'{df_case_file}\' is generated')

        df_anal_column, df_anal_line = AnalMargin(df_case, sampleNum)
        # df_anal_column = newcolumn + anal_column
        # print(df_anal_column)
        if indexrow == 1:
            df_anal = pd.DataFrame(columns=df_anal_column)
            df_anal.loc[indexrow] = df_anal_line
        else:
            df_anal.loc[indexrow] = df_anal_line

    df_merged = pd.concat([df, df_anal], axis=1)
    # print(df_merged)
    df_anal_file = path + '\\' + filename + '_anal.csv'
    # print(df_anal_file)
    df_merged.to_csv(df_anal_file)
    print(f'Analysis file \'{df_anal_file}\' is generated')

