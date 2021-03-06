import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/10000/5E0C62ED-A0BA-E811-8C32-002590E7DE36.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/10000/6407A5DB-A9B1-E811-B39F-0CC47ABB518A.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/10000/8C0001B2-FDB9-E811-840D-002590E7DFFC.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/10000/AE330D5A-1AB2-E811-AAE4-AC1F6B0DE3EE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/10000/CC7DA52C-E0B9-E811-8540-002590E7DE24.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/10000/D0EA1093-73B1-E811-9461-002590E7E010.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/10000/F2D3086C-48BA-E811-A7B5-0CC47ABB5178.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/10000/F6B5BDA2-3FBA-E811-963E-002590E7DF2A.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/020D9BBE-0FBB-E811-ACB2-002590E7E02E.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/049101F9-FCBA-E811-87B8-0CC47A1DF806.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/04F3D6B0-D1BA-E811-8C0E-AC1F6B0DE2EC.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/26A4C4EB-DFBA-E811-9A06-002590E7E01A.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/2EA43C05-00BB-E811-BC4E-0CC47A1DF806.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/3012497A-EBBA-E811-8C66-0CC47ABD6C6C.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/305B1ADE-03BB-E811-9001-0CC47ABB518A.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/380ADDD7-F9BA-E811-9BB1-AC1F6B0DE3EE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/3ABB05AE-3DBB-E811-B274-F4E9D4AEC770.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/40F0D4F6-B8BA-E811-A428-002590E7D7E2.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/42FE83AB-9ABA-E811-A826-AC1F6B0DE2EC.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/4AD2E440-AABA-E811-967B-002590E7D7EA.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/566D1445-41B7-E811-9F8E-AC1F6B0DE2EC.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/60EB2CFF-3CB6-E811-A8B4-002590E7E010.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/76832223-EEBA-E811-B16D-002590E7DFEE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/8CFDEF2D-F4BA-E811-B24F-002590E7DFA2.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/A402428D-0CBB-E811-9CC8-AC1F6B0DE296.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/A6B4B88B-E8BA-E811-B065-AC1F6B0DE296.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/AA95A88D-CBBA-E811-B710-002590E7DFD6.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/B81539EA-D7BA-E811-990E-0CC47A1E0488.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/BC9D0816-F1BA-E811-B61F-0CC47A1E0488.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/E4643802-C3BA-E811-A05F-002590E7DE24.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/110000/F2B34CF6-85BA-E811-8AAB-AC1F6B0DE0A0.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/02C47A76-B4B8-E811-89F4-0CC47A1DF800.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/04133FB7-E9B9-E811-B2CC-002590E7DFFC.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/06981082-BFB1-E811-B216-AC1F6B0DE296.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/0A572F92-AAAC-E811-9CA6-002590E7E01A.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/1C20F5D1-3FB9-E811-A744-0CC47A1DF60C.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/207CC7CC-3FB9-E811-9077-AC1F6B0DE296.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/28B2FA8E-1ABA-E811-AD9C-0CC47A1DF818.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/2CB548B8-23BA-E811-9209-002590E7E00A.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/2CBFFFE1-F7B9-E811-AD43-0CC47A1DF7FE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/2EB63270-ACB9-E811-9BD5-002590E7D5AE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/32FC963E-0AB7-E811-A3D3-002590E7D7DE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/34229603-0CBA-E811-8316-002590E7DFFC.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/4E5777C7-35BA-E811-9A7B-AC1F6B0DE3EE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/50178D63-D0B5-E811-8BFD-0CC47A1DF818.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/542A3BA1-F1B9-E811-8C76-002590E7D7DE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/544B89AD-57BA-E811-9F9F-AC1F6B0DE2FA.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/5454162C-49B9-E811-8746-0CC47A1DF818.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/562830CE-9BB6-E811-92B8-0CC47A1DF60C.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/56B49B84-C9B2-E811-8C7E-002590E7DFE4.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/601060D6-95BA-E811-9AB9-002590E7DD98.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/647D8262-60B7-E811-B13A-0CC47A1DF818.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/7045B326-3CB8-E811-A62F-AC1F6B0DE0C4.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/7245B2A4-1FBA-E811-A253-AC1F6B0DE140.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/7C32B8CA-74BA-E811-864D-002590E7D7C2.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/7C87608C-10BA-E811-A442-002590E7DFFE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/8289C996-CCB9-E811-B369-002590E7DFFE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/90790B18-01BA-E811-A08A-002590E7DE24.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/96CECC71-12BA-E811-A00D-AC1F6B0DE0C4.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/A43BB9B3-EBB9-E811-B64B-AC1F6B0DE2FA.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/A4D65253-FEB9-E811-8BD6-002590E7DE24.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/AA607C77-25BA-E811-A325-002590E7E050.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/AC7CD292-DCB9-E811-A287-002590E7E07A.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/AE2B28CA-07BA-E811-8035-002590E7DE24.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/AE5A8887-93B9-E811-9A3D-0CC47ABB5178.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/AEADEFAF-1EBA-E811-A0B0-002590E7DF2A.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/BACC140F-3EB9-E811-A9EC-0CC47A1E0DC8.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/BADAD422-9CBA-E811-A693-AC1F6B0DE296.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/C29963E1-9BBA-E811-A6A8-F02FA768CB3C.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/D27E82DD-32B9-E811-A73F-0CC47ABD6C6C.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/D679BF4A-33BA-E811-B172-002590E7DE24.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/E4B6CE9C-E1B9-E811-B7A6-002590E7DFA2.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/E61F9DD3-D5B9-E811-98A8-002590E7E004.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/EA1232FC-EFB8-E811-BBF6-0CC47A1DF818.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/EA4C43AF-04BA-E811-860D-002590E7DE24.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/EC1982CE-54BA-E811-A069-AC1F6B0DE2FA.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/EEFB7217-3CBA-E811-B707-AC1F6B0DE296.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/F03C51E7-EEB1-E811-ABC8-0CC47A1E0DC8.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/F2EAB4B8-06BA-E811-9918-0CC47ABB518A.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/F422ADC7-60BA-E811-BEDC-AC1F6B0DE2EC.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/F46E2959-33B1-E811-BB73-0CC47A1DF64E.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/70000/F80AE21B-B8B6-E811-981C-002590E7DE26.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/04930595-BFB5-E811-9CD9-FA163E52D5D9.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/04B89F09-E1BA-E811-BEB5-002590E7E01A.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/0E37CABB-88BC-E811-94CF-001E67E68BBD.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/1273F58D-0BBB-E811-8473-002590E7D7CE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/140B9EE2-65B5-E811-8155-FA163EBEAA03.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/143698A3-75B5-E811-B40D-FA163E31FE92.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/16F068DF-9BB2-E811-8E9B-1C6A7A26D1E3.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/187D266F-E2B2-E811-A002-FA163E5AD47B.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/18A7CD97-66B2-E811-B84D-0CC47AD98D06.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/1A6A2993-23BB-E811-A828-AC1F6B0DE362.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/1C437643-36B2-E811-92C2-24BE05CE6D61.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/1CE1E7F3-ECB3-E811-A109-0025901D08B0.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/1E5E210C-96B2-E811-BA0E-0CC47A57D13E.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/220B0136-56B5-E811-A30A-FA163E030AB8.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/269602F9-B4B2-E811-AAA7-E0071B6CAD00.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/286038DF-76B3-E811-83AE-D067E5F91B8A.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/2A0EB47A-BAB2-E811-86A3-002590A2BCBC.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/3015AF7C-97B2-E811-A81D-0CC47AD98B90.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/30926F84-DEB2-E811-81EB-0CC47AD98BC6.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/32796C25-0CB3-E811-9DEE-FA163E21F1D8.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/3457232B-D1BA-E811-8B78-AC1F6B0DE362.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/34C6EB45-A3B4-E811-AEF8-44A8423524BC.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/34F50272-14B3-E811-A6FC-0CC47AD98CEA.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/3ACB9833-78B2-E811-86A9-002590D9D8AC.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/3C27EF21-A8B2-E811-9B76-008CFA111320.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/3EB06A4A-B2B5-E811-A03F-FA163E13E98D.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/3EC019CC-E0B4-E811-869B-5065F381F291.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/3EC6DC2D-88B5-E811-A696-FA163E72348A.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/407A43D7-71B5-E811-B2A4-FA163E8BD266.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/40FA8A3F-17B3-E811-B542-002590D9D8B2.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/4462ADA8-4AB5-E811-94BA-FA163E9A6701.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/4637EFE4-7FB2-E811-AA95-1866DA7F9780.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/48C6CD30-6CB5-E811-AA6F-FA163E0D3ADE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/4A6DEE77-59B2-E811-83D2-3CFDFE63DF40.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/4A7A6B94-62B2-E811-B908-E0071B749C40.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/4AD3FD6E-BAB2-E811-B60E-FA163E43C73F.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/4E99B703-8EB2-E811-81B7-EC0D9A0B31B0.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/4ED946D1-5FB2-E811-9CB2-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/525F4A7D-5AB5-E811-AE1E-FA163E75DC14.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/542F5B14-EFBA-E811-882E-002590E7E02E.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/5489B669-7CB4-E811-AC69-0CC47A7C3444.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/585E022A-CBB2-E811-94E8-90B11C2CB7A9.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/5C4B3EE0-49B5-E811-AA4E-FA163E4C2F48.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/6008CDB1-EEB2-E811-9D09-FA163E235946.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/6046F9F4-16B5-E811-8A6A-0006F630D227.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/622AFC92-80B5-E811-897E-FA163EEB146C.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/62667B97-91BC-E811-B47F-0CC47A4D764C.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/6639DC8F-EFBA-E811-B1A3-002590E7D7EA.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/66D9B9BC-7AB2-E811-938B-0CC47A6C0716.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/68223762-8FB2-E811-923E-1C6A7A2637A3.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/6A162026-F8BA-E811-AFCE-0CC47A1E089C.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/6A9CF613-3DB3-E811-9343-FA163E5A65BE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/6C78ACBC-0FBD-E811-A604-008CFAC93F38.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/6CB0D7D9-41B5-E811-8748-FA163E355192.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/703D2A36-B4B2-E811-99DB-842B2B6AECDD.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/70DCD171-46B2-E811-BA4C-24BE05CE1E11.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/723F02E6-93B5-E811-AD5A-FA163E838DEE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/74ACA57A-60B5-E811-A802-FA163EC47258.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/74BCB60C-6AB2-E811-8DBA-0CC47AA992AC.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/7606CF07-9EBA-E811-9894-002590E7E02E.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/7613F667-B1B3-E811-9544-EC0D9A8222DE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/786ED5C8-0FBD-E811-934D-0CC47AA53D64.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/7AE15814-72B2-E811-AB47-EC0D9A0B3380.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/7CE54430-6BB5-E811-AD6D-FA163EA2F5B5.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/806CFE1E-D6B2-E811-A2B4-5065F38152E1.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/80DA4593-28B4-E811-BD31-FA163E7BDF55.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/82A86768-A1B5-E811-AD4F-FA163E2DB948.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/8457A207-88B2-E811-B527-0CC47A2B04B6.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/888F115C-5AB3-E811-AB15-0CC47AA98F9A.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/8CBB2503-8EB2-E811-BEC4-5065F38122A1.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/90ACE57C-06BB-E811-9735-002590E7E004.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/92AD8E01-06B3-E811-B7CF-EC0D9A0B3190.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/98C1774F-DFB5-E811-8F92-FA163E911768.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/9C5237A4-BAB3-E811-9C74-3CFDFE63D320.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/9E97B0D0-58B5-E811-99BD-FA163E8058DA.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/A246FE02-8DBC-E811-B8C1-02163E00C3C7.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/A41A85D4-8BB2-E811-A35B-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/A860242E-9BB5-E811-B085-FA163E677F25.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/AA242678-A0B2-E811-9539-0CC47A2B0214.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/AEC0355A-52B5-E811-A140-FA163E55D937.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/B0DB69CD-E6BB-E811-9C2B-002590E7D7E2.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/B210F74C-36B5-E811-A1CA-FA163E07DE6F.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/BCC72C70-77B4-E811-8DF8-0025905A48D6.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/BCF3736C-BDB3-E811-B792-008CFAC916B4.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/BE557607-12B3-E811-A423-FA163EF467AB.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/C2EBD284-2CBB-E811-93FD-0CC47ABD6C6C.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/CC4DDEAE-4DB2-E811-91B5-002590E3A212.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/D044DC83-E5BA-E811-91CD-AC1F6B0DE2EC.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/D04EC595-7ABC-E811-8756-3CFDFE635DC0.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/D0833C2D-2FB5-E811-901B-FA163E3516A2.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/D0D768D9-61B5-E811-BEA5-FA163E8058DA.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/D410221F-6AB2-E811-8E9A-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/D8008AFE-CBBA-E811-8CF9-AC1F6B0DE2EC.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/D8472C4D-D3B2-E811-AFA6-842B2B6AECDD.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/DCA5AD56-59B3-E811-959F-AC1F6B0DE3EE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/DEAAA560-4EB5-E811-9259-FA163E2EF64A.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/E05F180C-D9B4-E811-B8F1-0CC47A4C8E22.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/E4238831-EBB3-E811-A9AE-002590D9D8BA.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/E8B03EE6-6DBC-E811-B2CA-24BE05C44BB1.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/EA4A9D01-C3BA-E811-AC08-0CC47A1DF7E8.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/EE32B199-14B3-E811-A3EB-0CC47A4C8E64.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/EE82DB07-CABA-E811-8DE3-AC1F6B0DE2FA.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/F2F6734B-DFBA-E811-B983-002590E7D7DE.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/F41243A0-B1BA-E811-8478-0CC47ABD6C6C.root',
       '/store/mc/RunIIFall17MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/80000/FA0BB6B5-BEB2-E811-A095-002590D9D8C4.root',
] )
