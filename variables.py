# variables

#variables = {}

variables['BDTOutput'] = {
     'name': 'WW_against_top_bg_BDT(Entry$,0)',
#     'range' : ([-0.50,-0.25,-0.15,0.,0.15,0.25,0.35,0.50,0.80],),
     'range' : (10,-1,1),
     'xaxis' : 'MVA discriminant WW',
     'fold' : 3,
     'linesToAdd' : ['.L /afs/cern.ch/user/s/ssaumya/Projects/WW_Analysis_Work/WW_Cuts_Optimization/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/WW/FullRunII/Full2017_v7/BDT_Application/WW_against_top_bg_BDT.C']
}  #change the path of macro


variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }

variables['mll']  = {   'name': 'mll',
                        'range' : (30, 0,300),
                        'xaxis' : 'm_{ll} [GeV]',
                        'fold' : 0
                        }

variables['mth']  = {   'name': 'mth',
                        'range' : (30, 0,300),
                        'xaxis' : 'm_{T}^{H} [GeV]',
                        'fold' : 0
                        }

variables['ptll']  = {   'name': 'ptll',
                        'range' : (20, 0,200),
                        'xaxis' : 'p_{T}^{ll} [GeV]',
                        'fold' : 0
                        }

variables['puppimet']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (20,0,200),
                        'xaxis' : 'puppimet [GeV]',
                        'fold'  : 3
                        }

variables['njet']  = {
                        'name': 'Sum$(CleanJet_pt>30)',
                        'range' : (5,0,5),
                        'xaxis' : 'Number of jets',
                        'fold' : 2   
                        }

variables['mtw2'] = {  'name'  : 'mtw2',    
                       'range' : (25,0,500),
                       'xaxis' : 'm_{T}^{W2}', 
                       'fold'  : 3
                    }
						  
variables['mtw2_1'] = {  'name'  : 'mtw2',    
                         'range' : (50,0,500),
                         'xaxis' : 'm_{T}^{W2}', 
                         'fold'  : 3
                      }

variables['pt1']  = {   'name': 'Lepton_pt[0]',
                        'range' : (20,20,100),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 0
                        }

variables['pt2']  = {   'name': 'Lepton_pt[1]',
                        'range' : (20,10,100),
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 0
                        }

variables['eta1']  = {  'name': 'Lepton_eta[0]',
                        'range' : (20,-3,3),
                        'xaxis' : '#eta 1st lep',
                        'fold'  : 3
                        }

variables['eta2']  = {  'name': 'Lepton_eta[1]',
                        'range' : (20,-3,3),
                        'xaxis' : '#eta 2nd lep',
                        'fold'  : 3
                        }

variables['phi1']  = {  'name': 'Lepton_phi[0]',
                        'range' : (20,-3.2,3.2),
                        'xaxis' : '#phi 1st lep',
                        'fold'  : 3
                        }

variables['phi2']  = {  'name': 'Lepton_phi[1]',
                        'range' : (20,-3.2,3.2),
                        'xaxis' : '#phi 2nd lep',
                        'fold'  : 3
                        }

variables['jetpt1']  = {
                        'name': '(Sum$(CleanJet_pt>30)>0)*(Alt$(CleanJet_pt[0], 0)) - (Sum$(CleanJet_pt>30)==0)*99',
                        'range' : (20,0,200),
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 2   
                        }

variables['jetpt2']  = {
                        'name': '(Sum$(CleanJet_pt>30)>0)*(Alt$(CleanJet_pt[1], 0)) - (Sum$(CleanJet_pt>30)==0)*99',
                        'range' : (20,0,200),
                        'xaxis' : 'p_{T} 2nd jet',
                        'fold' : 2  
                        }

variables['jeteta1']  = {  'name': '(Sum$(CleanJet_pt>30)>0)*(Alt$(CleanJet_eta[0], 0)) - (Sum$(CleanJet_pt>30)==0)*99',
                        'range' : (20,-5.0,5.0),
                        'xaxis' : '#eta 1st jet',
                        'fold'  : 0
                        }

variables['jeteta2']  = {  'name': '(Sum$(CleanJet_pt>30)>1)*(Alt$(CleanJet_eta[1], 0)) - (Sum$(CleanJet_pt>30)<=1)*99',
                        'range' : (20,-5.0,5.0),
                        'xaxis' : '#eta 2nd jet',
                        'fold'  : 0
                        }
