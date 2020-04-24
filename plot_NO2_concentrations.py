# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:43:11 2020

@author: rikis
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#Pot ser hauràs de treure l'estació de Vall Hebron d'aquesta llista si no hi han dades per les setmanes següents
#Hauràs d'utilitzar el mateix format per nomenar les estacions en els arxius csv si vols que funcioni el codi
ZBE_stations = ['Eixample', 'Gracia', 'Ciutadella', 'Poblenou', 'Sants', 'VallHebron', 'ObsFabra', 'PalauReial', 'Hospitalet', 'SantAdria']
ZBE_titles = ['Barcelona (Eixample)', 'Barcelona (Gràcia - Sant Gervasi)', 'Barcelona (Ciutadella)', 'Barcelona (Poblenou)', 'Barcelona (Sants)', "Barcelona (Vall d'Hebron)", 'Barcelona (Observatori Fabra)', 'Barcelona (Palau Reial)', "l'Hospitalet de Llobregat", 'Sant Adrià de Besòs']

noZBE_stations = ['PratJardins', 'PratSagnier', 'Viladecans', 'SantCugat', 'SantaColoma', 'Badalona', 'Gava', 'Montcada', 'Barbera', 'SantAndreu', 'Palleja']
noZBE_titles = ['el Prat de Llobregat (Jardins de la Pau)', 'el Prat de Llobregat (CEM Sagnier)', 'Viladecans', 'Sant Cugat del Vallès', 'Santa Coloma de Gramenet', 'Badalona', 'Gavà', 'Montcada i Reixac', 'Barberà del Vallès', 'Sant Andreu de la Barca', 'Pallejà']

stations = ZBE_stations + noZBE_stations
stations_titles = ZBE_titles + noZBE_titles

     
def make_plot_with_errorbars(station,fig_name):
    #Aquí poses una altra línia de data6 = pd.read_csv(*) on * és la direcció del arxiu csv per l'estació station
    data1 = pd.read_csv('./Dades_XVPCA/Dades_XVPCA_'+station+'_NO2_2020-03-16.csv')
    data2 = pd.read_csv('./Dades_XVPCA/Dades_XVPCA_'+station+'_NO2_2020-03-23.csv')
    data3 = pd.read_csv('./Dades_XVPCA/Dades_XVPCA_'+station+'_NO2_2020-03-30.csv')
    data4 = pd.read_csv('./Dades_XVPCA/Dades_XVPCA_'+station+'_NO2_2020-04-06.csv')
    data5 = pd.read_csv('./Dades_XVPCA/Dades_XVPCA_'+station+'_NO2_2020-04-13.csv')
    
    #Aquí has d'afegir una altra línia si s'inclou un altre mes que no sigui Març o Abril
    last_year_month3 = pd.read_csv('./Dades_XVPCA/Dades_XVPCA_'+station+'_NO2_2019-Marc.csv')
    last_year_month4 = pd.read_csv('./Dades_XVPCA/Dades_XVPCA_'+station+'_NO2_2019-Abril.csv')
    
    #Aquí has d'afegir una altra línia per guardar les 24 mitjanes o medianes de la nova setmana
    mean1 = []
    mean2 = []
    mean3 = []
    mean4 = []
    mean5 = []
    
    #Aquí has d'afegir una altra línia per les mitjanes del nou mes si cal
    last_year_mean3 = []
    last_year_mean4 = []
    
    #Amb aquest valor adjustes els percentils que sortiran a la figura (amb per = 0.1 surten el 10% i el 90%)
    per = 0.1

    #Aquí hauràs d'afegir una nova línia per guardar els nous percentils de la nova setmana
    percentile1 = [[],[]]
    percentile2 = [[],[]]
    percentile3 = [[],[]]
    percentile4 = [[],[]]
    percentile5 = [[],[]]

    #Aquí hauràs d'afegir una altra línia si s'inclou un altre mes
    last_year_percentile3 = [[],[]]
    last_year_percentile4 = [[],[]]

    for i in range(1,25):
        #Aquí hauràs d'afegir 3 noves línies per calcular la mitjana/mediana i els percentils de la nova setmana
        mean1.append(data1['H'+str(i).zfill(2)].median())
        percentile1[0].append(data1['H'+str(i).zfill(2)].quantile(q=per))
        percentile1[1].append(data1['H'+str(i).zfill(2)].quantile(q=1-per))
        
        mean2.append(data2['H'+str(i).zfill(2)].median())
        percentile2[0].append(data2['H'+str(i).zfill(2)].quantile(q=per))
        percentile2[1].append(data2['H'+str(i).zfill(2)].quantile(q=1-per))
        
        mean3.append(data3['H'+str(i).zfill(2)].median())
        percentile3[0].append(data3['H'+str(i).zfill(2)].quantile(q=per))
        percentile3[1].append(data3['H'+str(i).zfill(2)].quantile(q=1-per))
        
        mean4.append(data4['H'+str(i).zfill(2)].median())
        percentile4[0].append(data4['H'+str(i).zfill(2)].quantile(q=per))
        percentile4[1].append(data4['H'+str(i).zfill(2)].quantile(q=1-per))
        
        mean5.append(data5['H'+str(i).zfill(2)].median())
        percentile5[0].append(data5['H'+str(i).zfill(2)].quantile(q=per))
        percentile5[1].append(data5['H'+str(i).zfill(2)].quantile(q=1-per))
        
        
        #Aquí hauràs d'afegir 3 noves línies si hi han les dades d'un nou mes de l'any passat
        last_year_mean3.append(last_year_month3['H'+str(i).zfill(2)].median())
        last_year_percentile3[0].append(last_year_month3['H'+str(i).zfill(2)].quantile(q=per))
        last_year_percentile3[1].append(last_year_month3['H'+str(i).zfill(2)].quantile(q=1-per))
        
        
        last_year_mean4.append(last_year_month4['H'+str(i).zfill(2)].median())
        last_year_percentile4[0].append(last_year_month4['H'+str(i).zfill(2)].quantile(q=per))
        last_year_percentile4[1].append(last_year_month4['H'+str(i).zfill(2)].quantile(q=1-per))
        

    x = np.arange(1,25)
    xticks = np.arange(0, 25, 4)
    plt.style.use('seaborn-white')
    
    #Aquí es defineixen el nombre de subplots en la imatge. Per afegir un nou hauràs de canviar de 5 a 6. Si vols incrementar el tamany
    #de la figura canvia el figsize
    fig, ax = plt.subplots(1, 5, sharex='col', sharey='row', figsize=(12,6))
    plt.subplots_adjust(wspace=0.05)
    
    ax[0].set_ylabel('Concentració ($\mathrm{\mu g/m^3}$)', fontsize=15)
    ax[0].tick_params(axis='y', labelsize=14)
    
    #Per afegir el nou subplot hauràs d'afegir aquestes 10 línies i canviar el valor de ax[x]. També
    #has de canviar el de mean1, percentile1, i posar la sèrie que toqui per l'any passat. 
    ax[0].plot(x, mean1, color='b') #aquesta línia genera el plot de la setmana de confinament
    ax[0].plot(x, last_year_mean3, color='tab:orange') #aquesta genera el plot del mes de l'any anterior
    ax[0].fill_between(x, percentile1[0], percentile1[1], facecolor='blue', alpha=0.2) #Aquest genera el sombrejat dels percentils de la setmana de confinament
    ax[0].fill_between(x, last_year_percentile3[0], last_year_percentile3[1], facecolors='tab:orange', alpha=0.2) #Aquest el sombrejat dels percentils del mes anterior
    ax[0].set_title( '16-20 Març 2020',  fontsize=13) #Aquí hauràs de canviar el títol per posar les dates de la setmana
    ax[0].grid(axis='y', which='major')
    ax[0].hlines(40, -1, 25, colors='r')
    ax[0].set_xlim(0,25)
    ax[0].set_xticks(xticks)
    ax[0].tick_params(axis='x', labelsize=12)
    
    ax[1].plot(x, mean2, color='b')
    ax[1].plot(x, last_year_mean3, color='tab:orange')
    ax[1].fill_between(x, percentile2[0], percentile2[1], facecolor='blue', alpha=0.2)
    ax[1].fill_between(x, last_year_percentile3[0], last_year_percentile3[1], facecolors='tab:orange', alpha=0.2)
    ax[1].set_title('23-27 Març 2020', fontsize=13)
    ax[1].grid(axis='y', which='major')
    ax[1].hlines(40, -1, 25, colors='r')
    ax[1].set_xlim(0,25)
    ax[1].set_xticks(xticks)
    ax[1].tick_params(axis='x', labelsize=12)
    
    ax[2].plot(x, mean3, color='b')
    ax[2].plot(x, last_year_mean3, color='tab:orange')
    ax[2].fill_between(x, percentile3[0], percentile3[1], facecolor='blue', alpha=0.2)
    ax[2].fill_between(x, last_year_percentile3[0], last_year_percentile3[1], facecolors='tab:orange', alpha=0.2)
    ax[2].set_title('30 Març-3 Abril 2020', fontsize=13)
    ax[2].grid(axis='y', which='major')
    ax[2].hlines(40, -1, 25, colors='r')
    ax[2].set_xlim(0,25)
    ax[2].set_xticks(xticks)
    ax[2].tick_params(axis='x', labelsize=12)
    
    ax[3].plot(x, mean4, color='b')
    ax[3].plot(x, last_year_mean4, color='tab:orange')
    ax[3].fill_between(x, percentile4[0], percentile4[1], facecolor='blue', alpha=0.2)
    ax[3].fill_between(x, last_year_percentile4[0], last_year_percentile4[1], facecolors='tab:orange', alpha=0.2)
    ax[3].set_title('6-10 Abril 2020', fontsize=13)
    ax[3].grid(axis='y', which='major')
    ax[3].hlines(40, -1, 25, colors='r')
    ax[3].set_xlim(0,25)
    ax[3].set_xticks(xticks)
    ax[3].tick_params(axis='x', labelsize=12)

    ax[4].plot(x, mean5, color='b')
    ax[4].plot(x, last_year_mean4, color='tab:orange')
    ax[4].fill_between(x, percentile5[0], percentile5[1], facecolor='blue', alpha=0.2)
    ax[4].fill_between(x, last_year_percentile4[0], last_year_percentile4[1], facecolors='tab:orange', alpha=0.2)
    ax[4].set_title('13-17 Abril 2020', fontsize=13)
    ax[4].grid(axis='y', which='major')
    ax[4].hlines(40, -1, 25, colors='r')
    ax[4].set_xlim(0,25)
    ax[4].set_xticks(xticks)
    ax[4].tick_params(axis='x', labelsize=12)
    
    fig.suptitle('Concentració $\mathrm{NO_2}$ ' + fig_name, fontsize=17)

    #plt.show()
    #Aquí posar la direcció de la carpeta on vols guardar els gràfics
    plt.savefig('./Plots_confinement/'+station+'_NO2_90')
    plt.close()
    
for i, station in enumerate(stations):
    make_plot_with_errorbars(station, stations_titles[i])
