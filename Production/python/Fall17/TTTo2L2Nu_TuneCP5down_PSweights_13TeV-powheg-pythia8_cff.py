import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/04179DED-4DA9-E811-AEF0-0CC47A6C1058.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/083F1FA7-A4A9-E811-A17A-0025901AFEA2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/08F642DE-42A9-E811-8755-0025901D08B0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/0A8D4C14-9CA9-E811-9F5F-0CC47AA98F9A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/0E6FC397-B6A9-E811-B912-0025901AFB36.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/0EF4C8F4-8DA9-E811-AC0B-0CC47A13D3A8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/12DB82DC-DDA9-E811-AF1E-003048F5ADF8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/14177B59-99A9-E811-9E2A-0CC47AA989BE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/16C717E6-B3A9-E811-8746-002590E2DD10.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/1AF6C93A-48A9-E811-A5D2-90B11C27E14D.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/1CA27076-C6A9-E811-80AE-0CC47AD991FA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/2683A642-48A9-E811-9D50-0CC47AD99116.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/2AFEFF3C-48A9-E811-B751-7C69F694C0B9.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/2C424138-48A9-E811-8794-0CC47AA98F96.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/3A9EECE6-C9A9-E811-BCF9-0CC47A13CB36.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/3CA7A58B-B6A9-E811-AC78-002590E39C46.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/446E4BF0-C3A9-E811-90C4-0CC47AD99116.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/46416B93-54A9-E811-A30A-0CC47AA989BA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/4674EB32-93A9-E811-8C54-0025907253C6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/48770529-BFA9-E811-88CE-0CC47A13D416.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/4E827897-A4A9-E811-A5EF-0CC47A2B04DE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/50973B95-D6A9-E811-B971-0025901D08F0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/5231B14E-48A9-E811-9DCC-0025901D08D2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/52558E9C-C6A9-E811-B144-0CC47A13D3B2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/5431C534-88A9-E811-BBC1-0CC47A2AECDC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/546944C8-42A9-E811-8FA4-0CC47AA98F98.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/564DFA9D-9EA9-E811-B71B-0CC47AA98F9A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/58DD0D26-A8A9-E811-9C47-0025907253C6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/62F46F3A-48A9-E811-9BD7-0CC47AA98F96.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/6A7192AC-D3A9-E811-BB78-0CC47A2AED0E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/6ADD2FC6-42A9-E811-94AC-0CC47AD9914C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/6E43EB6F-C3A9-E811-9F70-0CC47A13D416.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/706CA974-D0A9-E811-AEE5-0CC47A13D3B2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/70CB2C1B-93A9-E811-8C97-0025900EAB2A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/70EC3F42-88A9-E811-8FB7-0CC47A13D0F2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/72A02070-C3A9-E811-ADB8-0CC47A13D416.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/72FB425A-B1A9-E811-A1A0-0025901D08F0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/7423F53C-48A9-E811-8BD5-0CC47A6C115A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/74A37029-BFA9-E811-8966-0CC47A13D416.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/76662AD2-42A9-E811-9508-0CC47A13CD44.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/782F173D-48A9-E811-9FBE-7C69F694C0B9.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/7E468949-48A9-E811-9909-0025904AC2C6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/8011F2A3-C6A9-E811-BF4B-0CC47A6C06C4.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/827AC6F3-73A9-E811-8BED-0CC47AD98B94.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/84143A7B-6EA9-E811-8797-0CC47AA98F9A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/8619C4D6-95A9-E811-B216-0CC47AA989BE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/8AB0633F-48A9-E811-BE56-90B11C27F610.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/8AC71440-48A9-E811-9471-002590E2F9D4.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/8C8CE25D-90A9-E811-93C2-0CC47A6C115C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/902B4244-48A9-E811-92A3-0CC47A6C1818.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/965A4DEE-ADA9-E811-B1FD-0CC47A13D2BE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/982DABEA-C9A9-E811-9E94-0CC47A6C0716.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/98BABA3F-ABA9-E811-9C21-0CC47A2B0388.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/A218B2B1-7AA9-E811-A501-0CC47AD98C88.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/A238DF0F-A2A9-E811-AB2C-0025904A9472.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/AEA54D3C-48A9-E811-96A6-90B11C27E14D.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/AEE387A1-D3A9-E811-92C7-0CC47AA992B2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/B28EE586-C3A9-E811-A922-0CC47A13D416.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/B40D65FC-A7A9-E811-A552-0CC47A2B04DE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/B8212BF5-C1A9-E811-B2F5-0025904897C2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/BA7D033E-48A9-E811-9D55-0CC47A6C06C2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/BA95065D-90A9-E811-88BF-0CC47A6C115C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/BECFAEA8-C2A9-E811-B368-0CC47AD991FA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/C05B3A29-BFA9-E811-8B9C-0CC47A13D416.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/C6FFAF4E-48A9-E811-A2B6-0025901D08D2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/D868ECE7-C9A9-E811-8402-0CC47A13CB36.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/D8F70A6B-D0A9-E811-90C9-90B11C28232B.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/DE141A5C-85A9-E811-BA08-002590E1E9B8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/E0FDD245-B1A9-E811-A4E6-0CC47AD98D10.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/E27E6990-B6A9-E811-87E5-003048F5ADEE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/E29ED03B-48A9-E811-AC40-0CC47A6C14C8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/E4802F44-48A9-E811-B36B-0CC47A6C1818.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/E60C3E55-BDA9-E811-81D7-0025904897C2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/E6BF753F-48A9-E811-ADEF-0CC47A6C115A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/E8D93A40-48A9-E811-B588-002590E2F9D4.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/EA6ECA29-BFA9-E811-BE85-0CC47A13D416.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/EE4F233B-48A9-E811-94F3-0CC47AD98D74.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/F03AFE3B-48A9-E811-A9E7-0CC47A6C14C8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/F2182A6B-D0A9-E811-A602-90B11C28232B.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/F271DE90-B6A9-E811-9458-0025904A8ECA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/F6F90313-9CA9-E811-8A4A-0CC47AD98F78.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/F8585158-85A9-E811-921C-002590E2DD10.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/FA00FF4F-B3A9-E811-97A6-0CC47AD98D10.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/FAF854EE-ADA9-E811-B5F9-0CC47A13D2BE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/FCB4B8ED-73A9-E811-ACA6-0CC47AD99050.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/80000/FE0C37AE-C6A9-E811-ABC1-00259048812E.root',
] )
