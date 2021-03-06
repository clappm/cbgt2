import cbgt as cbgt
from frontendhelpers import *
from tracetype import *
import init_params as par
import popconstruct as popconstruct
import qvalues as qval
import generateepochs as gen
from agentmatrixinit import *
from agent_timestep import timestep_mutator, multitimestep_mutator
import pipeline_creation as pl_creat
import seaborn as sns
import matplotlib.pyplot as plt

figure_dir = "./Figures/"

def rename_columns(results):
    
    results['popdata']['newname'] = results['popdata']['name']+'_'+results['popdata']['action']
    new_names = dict()
    for i in results['popdata'].index[:-2]:
        temp = untrace(results['popdata']['newname'].iloc[i])
        #print(type(temp))
        if 'LIP' in temp:
            temp1 = "Cx_"+temp.split('_')[1]
            temp = temp1
        new_names[i] = temp
    new_names[i+1]='FSI_common'
    new_names[i+2]='CxI_common'
    results['popfreqs'] = results['popfreqs'].rename(columns=new_names)
    
    return results


def plot_fr(results):
    
    # Plot Population firing rates
    results_local = results['popfreqs'].copy()
    results_local_melt = results_local.melt("Time (ms)")
    
    
    results_local_melt["nuclei"] = [ x.split('_')[0]  for x in results_local_melt["variable"]]
    results_local_melt["channel"] = [ x.split('_')[1]  for x in results_local_melt["variable"]]
    #print(results_local_melt)
    results_local_melt = results_local_melt.rename(columns={"value":"firing_rate"})
    g1 = sns.relplot(x="Time (ms)", y ="firing_rate", hue="channel",col="nuclei",data=results_local_melt,col_wrap=3,kind="line",facet_kws={'sharey': False, 'sharex': True})
    g1.fig.savefig(figure_dir+'ActualFR.png', dpi=400)
    
