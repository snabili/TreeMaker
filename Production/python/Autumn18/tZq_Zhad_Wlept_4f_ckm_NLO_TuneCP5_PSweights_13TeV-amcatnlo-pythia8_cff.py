import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/23BDF99A-D43A-E840-A418-FF0D8A568DDB.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/32EB4022-D534-3B4F-88DE-C115C48352AE.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/42D194E8-894B-6B4D-A467-A5DF8C4656B1.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/9C84A5AA-EFCA-8A4A-A8C2-CD0766103B6E.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/A68A5E70-C65A-CB41-8B80-64392841D8AE.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/B4F412F9-2883-5A4A-9B0C-7F1BEE2EC2EC.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/B5635C8B-A168-C448-82E6-CEA3E30E78F6.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/C11714EE-E0B6-7547-960D-19BBB2F2A1C3.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/C90E3480-ECF5-EB41-A68B-55DE9581FFB0.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/D8006F32-CFC0-1443-AE0C-57557CC47796.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/EF7801A7-9187-584B-B334-5BB2CD49D78C.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/F2014CA3-B9B5-C145-92A3-6ABA9EAD132F.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/F5C36186-5205-A746-90AE-235D43D7F32D.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/260000/FE874065-4CE2-AF45-8F4B-AF8B66885785.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/01EA3160-3D35-B540-B73D-9B23AC36F5EF.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/01FFAFB0-AB26-164F-AE9A-4F870E0A1EA5.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/020416D4-3001-C545-9C72-E94C25D9339E.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/0272B3E6-5712-6C47-9B9C-E4FAC63EADE8.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/02A4BC2B-A785-CE42-842F-D35DAC139512.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/02D2316F-4201-9741-8973-C897CF4CBF15.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/046698A2-2A82-D148-84FE-A9D722C977C1.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/05D9D148-51E7-DD49-882E-5BE8FE21C64A.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/06C62972-1188-A34B-8DCA-907EC0A10E2E.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/06ECB50E-8AA7-A040-AF81-753D62AD07D2.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/0889540E-5414-9748-AA0F-BABFE32C795F.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/0957AD0E-06CC-4C45-9DCE-94E88E4E1F2C.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/095EBFE1-2F6B-4244-B376-FD4A14F9FD15.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/0A247CA5-D037-9343-98D8-12C6200665DB.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/0FD7C6FF-C0E6-7C44-90E3-28911FE2094D.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/14A7F783-EEE4-1D41-BA8A-784C832D55EB.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/154FAE86-DD65-9F49-8076-3A7785BABB1A.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/15FA5D1D-EB6A-D04A-A57E-A920C5982572.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/19A9C074-D524-0D41-AE70-894B14E4CD6C.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/1A083CAF-3AD0-7449-8AFD-541672A5E54C.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/1B0042BC-65CF-344A-B098-0C3B072E5583.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/1D72C578-920D-3046-B37C-265600949F80.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/1E1E19CB-6BE3-A144-8E1E-74C22E56ADAA.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/1EE6BA8F-E772-2445-A7D8-CF929ECFBAA3.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/1F47C903-2FC2-2D44-B274-D2DEE9F3B652.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/23D50139-1B85-1447-8AD0-7C968F8BE98E.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/2762C0CE-EA93-8544-8BC5-662B82F6F6E6.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/2ADF0A36-5BCA-3F4A-81BE-68B04A0C73EE.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/2C474249-CE14-964B-A19F-849024F4F018.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/2CAD00E2-B0BD-794D-B107-02688047D16D.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/2EB3BD06-E0A8-374F-8150-566A6F6F308A.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/313F05DF-304A-7A48-9D1C-D988241D2663.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/332BE7C1-B3D6-3047-B660-FA14DD0D1C37.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/34FD08C9-101A-A048-BC2D-3EAF6B148305.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/355E00DD-5817-9743-BDC2-7518D336DF3B.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/35CF913E-5BCB-A34B-9107-BB73C02892C7.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/37BB0B09-3D54-2448-BDF8-F8763EC225C0.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/39E30BE7-F133-7842-A4BC-9D3BAF2F7ADB.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/3A122F21-05EF-E442-8348-AF1FA8CA1DAB.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/3E9DEB18-4A99-EB4B-80B8-6FDEAADFB04F.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/3EB0A0BA-7685-F340-A840-F825F0E61CC1.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/42F259E8-B5AB-0142-B504-1328EC3126B0.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/434CFB79-D754-904A-990B-E8815E85D2DD.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/4373F493-5C15-C440-A086-D90EEBCB1F32.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/43CB6CFA-DC3E-3A44-B7F2-CB910ABD9A73.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/44942F5E-77F9-5440-BCE0-E9F3352D9543.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/4AE27639-FCB8-6843-B9D9-4CFFBF020ACD.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/4F8DBC94-F331-1245-AFC9-4950C1958CF8.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/5115F87A-67C1-BE4F-8417-0504B23FAA07.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/53B65C07-0B1D-CA4C-A885-03F6DC372D44.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/551365D9-E1DC-1545-A9EB-D957D18A50B6.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/56AAC9E7-2775-5642-AC1E-14424A6633F7.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/59B15074-CB78-FC41-B81F-1111E3D8385F.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/5C04F7D1-2AED-6F49-9E1D-56BBBBE90F31.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/5C1302C0-03A9-5A46-AEF1-87D21725000A.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/5D5B0D87-F51F-2248-8508-109E329FA920.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/62A27BAD-1F55-564E-9341-59C86FA3D642.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/63D2EF50-A42E-1443-BA14-8681B093234D.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/64F1F638-3A08-744D-A297-131177F98B25.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/64FB31A3-9BED-3849-B1B5-71B27C722F12.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/6880B759-A7E7-2041-91F1-7409CC2D5C97.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/68A023BC-CAE0-2440-9CB4-AAF1FC43FA2D.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/68F858C9-018E-9243-B470-40C517DF63EF.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/6968A156-119C-1347-B65A-2648F33F79C8.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/6B917420-C53E-8242-8E3E-C39A87ECA010.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/6C182088-607E-BF40-9FBC-9F584A1E10B5.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/6C39133F-25F9-8949-855D-1A75774D32D2.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/6C9FA2DA-CCE7-7B45-A079-8668F0073606.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/6D595AFC-6403-A942-9198-EEE0028E90C6.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/6D8224A9-219F-D14C-AFA4-709D326C00C7.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/73B55E07-2248-AE41-9582-44B68D631CD4.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/73DA168A-A3CE-874C-979C-E8C15599FB3D.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/76B8903E-9214-9547-BE9B-E948A7676BF9.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/789211DA-3CE7-A246-B600-8B317A5072A9.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/835AA039-0ADE-564E-8D77-FBC2FF65F061.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/8604781B-57A2-C64C-A87A-F95DDDFA2F91.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/86297A5B-917D-3B47-AB3B-4C51D41DCE99.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/88E9ABB2-4BAF-4E4F-A1FF-A81BA6F6E5F9.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/8A4C4430-3452-6547-AB62-2F178BB7BD12.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/8AE18DF3-872B-294E-A7A8-AABFBE8AE9AF.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/8F0E20C6-336A-3941-957E-CB73C3684905.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/8F459DDA-AB17-3A49-9067-E9ABC190B609.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/90BE3499-2AA1-7245-863C-AF54A6D1E7B2.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/9317D002-FEE1-424F-852E-1D19C9BAE5FF.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/9598EF6C-B28C-FA46-A0FB-8BF6B50FA756.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/985098FE-1EF9-5B49-A7CA-7EC4FBE6F24F.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/9903BE7A-AB9F-384F-B63A-DF147F273775.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/99A152B7-B88F-6742-880D-F55F0FEF906B.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/99FA3A4C-3192-FB48-8221-2A4E8D5DF73C.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/A11FDE68-1F49-854B-8883-280B22A6A5EC.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/A1BEEABC-BA94-8546-BA91-5F5C3FDF7442.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/A208FE4B-3B3C-CB45-BC65-3BE3C1F31C8B.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/A22B126B-80C7-ED4A-AA8E-0E5DFE2B18DE.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/A4513B10-80B6-0843-A901-B569D6C34868.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/A637309D-E47A-9E43-B7AD-31264FD3B154.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/A65B2F99-8374-8649-BDC5-157D0ABF2E77.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/A739C916-5D22-554C-AF8C-97780344489C.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/A7993953-0692-5F44-9DB8-95511DBB0A3F.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/AB3EC9AD-5C02-824A-A7D1-9012D0EF83A6.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/AC2D63AC-6C6C-B14E-9579-FC187DE4BD80.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/AF05110A-A402-6D48-8FE4-8536726E9D8A.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/B01124C5-96DF-6A49-BC7B-8AC7AAAA7CE7.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/B2CC3E21-A64E-AF4D-BD69-E67B1C530451.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/B40876E6-30C8-BC44-AA7D-6AD8FD151E5E.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/B4B823E6-6A9A-3D4F-B4E9-A73C433609FA.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/B73A0E23-6A21-8444-B1CD-92FAEC80CE68.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/B7ECC85F-14E9-9845-9572-6783E0F17A39.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/BBF46301-8442-764A-A4BA-6C31C3F28DAF.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/C1605313-B618-6E43-A09E-3B9DE2D3F44E.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/C18C6EF8-A096-8F46-AF6D-8A55342152E9.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/C23F8E7A-33AC-444D-9D50-13341D2830D7.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/C280E390-26E3-0A45-AD9F-03C1200F0A52.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/C35B8ABB-700D-A843-9C1A-BFD5A8984905.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/C4C13DDB-F5A5-8B47-8768-4F21235729F6.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/C4CCDAF1-86B1-5D41-B71F-171D863CDE4A.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/CDA7CE86-0E62-604A-903E-6C53E10A24AD.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/CE1D257C-E60B-7342-9ADB-D16176D00BB1.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/CFD63AAB-2474-D646-874B-6758147A7805.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/D021CEC3-B273-C240-99C4-326F5537420B.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/D05AAD26-CE07-F041-AFEC-4BA176E7D977.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/D0ECFA4E-9FE9-B84A-A5DD-79DFC9D9D53F.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/D13F3491-1A33-AC43-A9BC-1B765015D44A.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/D260B114-D973-AD4F-9D88-51DBC8D49D8A.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/D4222C1F-A5D5-4D48-B847-AB4CFC9C9CA5.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/D4E9661E-BA68-B541-B0C9-EEC8D9AAE643.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/D7987BB3-0530-E640-B4CA-7EDC05BF4578.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/D847B88E-1FA0-CD44-9B9E-DA2C6C4A4E86.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/D8578081-4D87-DF4F-B1F1-5ABE92B48762.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/DB2ECB48-20F1-4043-A1EE-C18015330EE6.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/DC766F17-4E38-0440-8342-45CD4E09ED47.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/DD3EB2A9-BD62-A34A-8D60-AA949661CB14.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/E44A389F-11D4-A645-8381-2937FE814495.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/E6450A09-C185-3F47-BEC1-F15F4F7E9FDA.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/E74A3E18-389D-054C-ADB2-B7DA5A7A1C62.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/E84C8080-4BB6-A244-A095-A3A35EF01569.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/E9567FA4-5F76-2A40-A583-A384A549825B.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/EA28DD16-1850-404A-8CE7-D68491F79B76.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/ED8B270F-7385-F540-8532-0DCAD497A22A.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/F0193709-0311-BC47-A7DC-2D838D003EC2.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/F32AC692-49D4-9545-AD79-3BAA6EDC0E8E.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/F33A420A-530C-9D4F-923D-C3C3085CD8F2.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/F37EA872-AD58-C348-9231-802DB0214EED.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/F9B3DEC5-6044-5C40-93C0-469254E3B648.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/F9B57A70-B84E-9745-A93F-026C569A7F06.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/FCC2FEDB-4609-BF4A-8E6C-E264D924E5D0.root',
       '/store/mc/RunIIAutumn18MiniAOD/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/30000/FEF9EB05-D703-AD4A-9F7B-36CBA4FF1CA3.root',
] )