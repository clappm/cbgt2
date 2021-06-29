from frontendhelpers import *


def helper_paramset(params=None):
    if params is None:
        params = dict()

    celldefaults = {'N': 75,
                    'C': 0.5,
                    'Taum': 20,
                    'RestPot': -70,
                    'ResetPot': -55,
                    'Threshold': -50,
                    'RestPot_ca': -85,
                    'Alpha_ca': 0.5,
                    'Tau_ca': 80,
                    'Eff_ca': 0.0,
                    'tauhm': 20,
                    'tauhp': 100,
                    'V_h': -60,
                    'V_T': 120,
                    'g_T': 0,
                    'g_adr_max': 0,
                    'Vadr_h': -100,
                    'Vadr_s': 10,
                    'ADRRevPot': -90,
                    'g_k_max': 0,
                    'Vk_h': -34,
                    'Vk_s': 6.5,
                    'tau_k_max': 8,
                    'n_k': 0,
                    'h': 1, }

    if len(params) != 0:

        celldefaults.update(params)

    return celldefaults


def helper_popspecific(pops=None):
    if pops is None:
        pops = dict()

    popspecific = {'LIP': {'N': 204},
                   'FSI': {'C': 0.2, 'Taum': 10},
                   # should be 10 but was 20 due to bug
                   'GPeP': {'N': 750, 'g_T': 0.06, 'Taum': 20},
                   'STNE': {'N': 750, 'g_T': 0.06},
                   'LIPI': {'N': 186, 'C': 0.2, 'Taum': 10},
                   'Th': {'Taum': 27.78}}

    if len(pops) != 0:
        for key in pops.keys():
            for item in pops[key].keys():
                popspecific[key][item] = pops[key][item]

    return popspecific


def helper_receptordefaults(receps=None):
    if receps is None:
        receps = dict()

    receptordefaults = {'Tau_AMPA': 2,
                        'RevPot_AMPA': 0,
                        'Tau_GABA': 5,
                        'RevPot_GABA': -70,
                        'Tau_NMDA': 100,
                        'RevPot_NMDA': 0, }

    if len(receps) != 0:

        receptordefaults.update(receps)

    return receptordefaults


def helper_basestim(base=None):
    if base is None:
        base = dict()

    basestim = {'FSI': {
        'FreqExt_AMPA': 3.6,
        'MeanExtEff_AMPA': 1.55,
        'MeanExtCon_AMPA': 800},
        'LIPI': {
        'FreqExt_AMPA': 1.05,
        'MeanExtEff_AMPA': 1.2,
        'MeanExtCon_AMPA': 640},
        'GPi': {
        'FreqExt_AMPA': 0.8,
        'MeanExtEff_AMPA': 5.9,
        'MeanExtCon_AMPA': 800},
        'STNE': {
        'FreqExt_AMPA': 4.45,
        'MeanExtEff_AMPA': 1.65,
        'MeanExtCon_AMPA': 800},
        'GPeP': {
        'FreqExt_AMPA': 4,
        'MeanExtEff_AMPA': 2,
        'MeanExtCon_AMPA': 800,
        'FreqExt_GABA': 2,
        'MeanExtEff_GABA': 2,
        'MeanExtCon_GABA': 2000},
        'D1STR': {
        'FreqExt_AMPA': 1.3,
        'MeanExtEff_AMPA': 4,
        'MeanExtCon_AMPA': 800},
        'D2STR': {
        'FreqExt_AMPA': 1.3,
        'MeanExtEff_AMPA': 4,
        'MeanExtCon_AMPA': 800},
        'LIP': {
        'FreqExt_AMPA': 2.2,
        'MeanExtEff_AMPA': 2,
        'MeanExtCon_AMPA': 800},
        'Th': {
        'FreqExt_AMPA': 2.2,
        'MeanExtEff_AMPA': 2.5,
        'MeanExtCon_AMPA': 800}, }

    if len(base) != 0:
        for key in base.keys():
            for item in base[key].keys():
                basestim[key][item] = base[key][item]

    return basestim


def helper_dpmndefaults(dpmns=None):
    if dpmns is None:
        dpmns = dict()

    dpmndefaults = {'dpmn_tauDOP': 2,
                    'dpmn_alpha': 0.3,
                    'dpmn_DAt': 0.0,
                    'dpmn_taum': 1e100,
                    'dpmn_dPRE': 0.8,
                    'dpmn_dPOST': 0.04,
                    'dpmn_tauE': 15,
                    'dpmn_tauPRE': 15,
                    'dpmn_tauPOST': 6,
                    'dpmn_wmax': 0.3,
                    'dpmn_w': 0.1286,
                    'dpmn_Q1': 0.0,
                    'dpmn_Q2': 0.0,
                    'dpmn_m': 1.0,
                    'dpmn_E': 0.0,
                    'dpmn_DAp': 0.0,
                    'dpmn_APRE': 0.0,
                    'dpmn_APOST': 0.0,
                    'dpmn_XPRE': 0.0,
                    'dpmn_XPOST': 0.0}

    if len(dpmns) != 0:

        dpmndefaults.update(dpmns)

    return dpmndefaults


def helper_d1defaults(d1=None):
    if d1 is None:
        d1 = dict()

    d1defaults = {'dpmn_type': 1,
                  'dpmn_alphaw': 55 / 3.0,  # ???
                  'dpmn_a': 1.0,
                  'dpmn_b': 0.1,
                  'dpmn_c': 0.05, }

    if len(d1) != 0:

        d1defaults.update(d1)

    return d1defaults


def helper_d2defaults(d2=None):
    if d2 is None:
        d2 = dict()

    d2defaults = {'dpmn_type': 2,
                  'dpmn_alphaw': -45 / 3.0,
                  'dpmn_a': 0.5,
                  'dpmn_b': 0.005,
                  'dpmn_c': 0.05, }

    if len(d2) != 0:

        d2defaults.update(d2)

    return d2defaults


def helper_actionchannels(channels=None):
    if channels is None:
        channels = dict()

    actionchannels = {'action': [1, 2], }

    if len(channels) != 0:

        actionchannels.update(channels)

    return actionchannels
