// -*- C++ -*-
//
// Package:    GoodJetsProducer
// Class:      GoodJetsProducer
//
/**\class GoodJetsProducer GoodJetsProducer.cc RA2Classic/GoodJetsProducer/src/GoodJetsProducer.cc
 *
 * Description: [one line class summary]
 *
 * Implementation:
 *     [Notes on implementation]
 */
//
// Original Author:  Arne-Rasmus Draeger,68/111,4719,
//         Created:  Thu Apr 17 10:49:52 CEST 2014
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include <DataFormats/Math/interface/deltaR.h>
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "PhysicsTools/PatAlgos/plugins/PATJetProducer.h"
#include <DataFormats/PatCandidates/interface/Photon.h>
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include <TVector2.h>
//
// class declaration
//

class GoodJetsProducer : public edm::EDFilter {
public:
   explicit GoodJetsProducer(const edm::ParameterSet&);
   ~GoodJetsProducer();
   
   static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
   
private:
   virtual void beginJob() override;
   virtual bool filter(edm::Event&, const edm::EventSetup&) override;
   virtual void endJob() override;
   
   virtual void beginRun(edm::Run&, edm::EventSetup const&);
   virtual void endRun(edm::Run&, edm::EventSetup const&);
   virtual void beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
   virtual void endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
   edm::InputTag JetTag_;
   edm::InputTag MuonTag_, ElecTag_, IsoElectronTrackTag_, IsoMuonTrackTag_, IsoPionTrackTag_, PhotonTag_;
   double maxEta_;
   double maxNeutralFraction_, maxPhotonFraction_, minChargedFraction_, maxChargedEMFraction_, maxPhotonFractionHF_;
   double maxNeutralFractionPBNR_, maxPhotonFractionPBNR_, maxNeutralFractionTight_, maxPhotonFractionTight_;
   int minNconstituents_, minNneutrals_, minNcharged_;
   double jetPtFilter_;
   bool saveAll_, ExcludeLeptonIsoTrackPhotons_, TagMode_;
   double JetConeSize_;
   double deltaR(double eta1, double phi1, double eta2, double phi2);
   
   // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
using namespace pat;
GoodJetsProducer::GoodJetsProducer(const edm::ParameterSet& iConfig)
{
   TagMode_ = iConfig.getParameter<bool> ("TagMode");
   JetTag_ = iConfig.getParameter<edm::InputTag>("JetTag");
   maxEta_ = iConfig.getParameter <double> ("maxJetEta");
   minNconstituents_ = iConfig.getParameter <int> ("minNconstituents");
   minNneutrals_ = iConfig.getParameter <int> ("minNneutrals");
   minNcharged_ = iConfig.getParameter <int> ("minNcharged");
   maxNeutralFraction_ = iConfig.getParameter <double> ("maxNeutralFraction");
   maxPhotonFraction_ = iConfig.getParameter <double> ("maxPhotonFraction");
   maxPhotonFractionHF_ = iConfig.getParameter <double> ("maxPhotonFractionHF");
   maxNeutralFractionPBNR_ = iConfig.getParameter <double> ("maxNeutralFractionPBNR");
   maxPhotonFractionPBNR_ = iConfig.getParameter <double> ("maxPhotonFractionPBNR");
   maxNeutralFractionTight_ = iConfig.getParameter <double> ("maxNeutralFractionTight");
   maxPhotonFractionTight_ = iConfig.getParameter <double> ("maxPhotonFractionTight");
   minChargedFraction_ = iConfig.getParameter <double> ("minChargedFraction");
   maxChargedEMFraction_ = iConfig.getParameter <double> ("maxChargedEMFraction");
   jetPtFilter_ = iConfig.getParameter <double> ("jetPtFilter");
   saveAll_ = iConfig.getParameter <bool> ("SaveAllJets");  
   
   ExcludeLeptonIsoTrackPhotons_ = iConfig.getParameter <bool> ("ExcludeLepIsoTrackPhotons");
   MuonTag_ = iConfig.getParameter<edm::InputTag>("MuonTag");
   ElecTag_ = iConfig.getParameter<edm::InputTag>("ElecTag");
   IsoElectronTrackTag_ = iConfig.getParameter<edm::InputTag>("IsoElectronTrackTag");
   IsoMuonTrackTag_ = iConfig.getParameter<edm::InputTag>("IsoMuonTrackTag");
   IsoPionTrackTag_ = iConfig.getParameter<edm::InputTag>("IsoPionTrackTag");
   PhotonTag_ = iConfig.getParameter<edm::InputTag>("PhotonTag");
   JetConeSize_ = iConfig.getParameter <double> ("JetConeSize");
   
   produces<std::vector<Jet> >();
   produces<bool>("JetID");
   produces<bool>("Loose");
   produces<bool>("Tight");
   produces<bool>("PBNR");
   produces<std::vector<bool> >("JetIDMask");
   produces<std::vector<bool> >("JetLooseMask");
   produces<std::vector<bool> >("JetTightMask");
   produces<std::vector<bool> >("JetPBNRMask");
}


GoodJetsProducer::~GoodJetsProducer()
{
   
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)
   
}


//
// member functions
//

// ------------ method called to produce the data  ------------
bool
GoodJetsProducer::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   // load to be excluded leptons, isotracks and photons
   edm::Handle<edm::View<pat::Muon> > muonHandle;
   iEvent.getByLabel(MuonTag_, muonHandle);
   if(ExcludeLeptonIsoTrackPhotons_ && !muonHandle.isValid()) std::cout<<"Warning Muon Tag not valid in GoodJetSelector: "<<MuonTag_<<std::endl;
   
   edm::Handle<edm::View<pat::Electron> > eleHandle;
   iEvent.getByLabel(ElecTag_, eleHandle);
   if(ExcludeLeptonIsoTrackPhotons_ && !eleHandle.isValid()) std::cout<<"Warning elec Tag not valid in GoodJetSelector: "<<ElecTag_<<std::endl;
   
   edm::Handle<edm::View<pat::PackedCandidate> > isoElectronTrackHandle;
   iEvent.getByLabel(IsoElectronTrackTag_, isoElectronTrackHandle);
   if(ExcludeLeptonIsoTrackPhotons_ && !isoElectronTrackHandle.isValid()) std::cout<<"Warning isoelectrontrack Tag not valid in GoodJetSelector: "<<IsoElectronTrackTag_<<std::endl;
   
   edm::Handle<edm::View<pat::PackedCandidate> > isoMuonTrackHandle;
   iEvent.getByLabel(IsoMuonTrackTag_, isoMuonTrackHandle);
   if(ExcludeLeptonIsoTrackPhotons_ && !isoMuonTrackHandle.isValid()) std::cout<<"Warning isomuontrack Tag not valid in GoodJetSelector: "<<IsoMuonTrackTag_<<std::endl;
   
   edm::Handle<edm::View<pat::PackedCandidate> > isoPionTrackHandle;
   iEvent.getByLabel(IsoPionTrackTag_, isoPionTrackHandle);
   if(ExcludeLeptonIsoTrackPhotons_ && !isoPionTrackHandle.isValid()) std::cout<<"Warning isopiontrack Tag not valid in GoodJetSelector: "<<IsoPionTrackTag_<<std::endl;
   
   edm::Handle<std::vector<pat::Photon> > photonHandle;
   iEvent.getByLabel(PhotonTag_, photonHandle);
   if(ExcludeLeptonIsoTrackPhotons_ && !photonHandle.isValid()) std::cout<<"Warning Muon Tag not valid in GoodJetSelector: "<<PhotonTag_<<std::endl;
   
   std::auto_ptr<std::vector<Jet> > prodJets(new std::vector<Jet>());
   std::auto_ptr<std::vector<bool> > jetsVLoose(new std::vector<bool>());
   std::auto_ptr<std::vector<bool> > jetsLoose(new std::vector<bool>());
   std::auto_ptr<std::vector<bool> > jetsTight(new std::vector<bool>());
   std::auto_ptr<std::vector<bool> > jetsPBNR(new std::vector<bool>());
   bool result=true;
   bool resultLoose=true;
   bool resultPBNR=true;
   bool resultTight=true;
   edm::Handle< edm::View<Jet> > Jets;
   iEvent.getByLabel(JetTag_,Jets);
   if(Jets.isValid())
   {
      for(unsigned int i=0; i<Jets->size();i++)
      {
         if (std::abs(Jets->at(i).eta())>maxEta_) continue;
         float neufrac=Jets->at(i).neutralHadronEnergyFraction();//gives raw energy in the denominator
         float phofrac=Jets->at(i).neutralEmEnergyFraction();//gives raw energy in the denominator
         float chgfrac=Jets->at(i).chargedHadronEnergyFraction();
         float chgEMfrac=Jets->at(i).chargedEmEnergyFraction();
         int chgmulti=Jets->at(i).chargedMultiplicity();
         int neumulti=Jets->at(i).neutralMultiplicity();
         int nconstit=chgmulti+neumulti;
         bool skip=false;
         if(ExcludeLeptonIsoTrackPhotons_)
         {
            for(unsigned int m=0; m<muonHandle->size(); ++m)
            {
               if(std::abs(Jets->at(i).pt() - muonHandle->at(m).pt() ) / muonHandle->at(m).pt() <1 && deltaR(Jets->at(i).eta(),Jets->at(i).phi(),muonHandle->at(m).eta(),muonHandle->at(m).phi())<JetConeSize_ ) skip=true;
            }
            for(unsigned int e=0; e<eleHandle->size(); ++e)
            {
               if(std::abs(Jets->at(i).pt() - eleHandle->at(e).pt() ) / eleHandle->at(e).pt() <1 && deltaR(Jets->at(i).eta(),Jets->at(i).phi(),eleHandle->at(e).eta(),eleHandle->at(e).phi())<JetConeSize_ ) skip=true;
            }
            for(unsigned int e=0; e<isoElectronTrackHandle->size(); ++e)
            {
               if(std::abs(Jets->at(i).pt() - isoElectronTrackHandle->at(e).pt() ) / isoElectronTrackHandle->at(e).pt() <1 && deltaR(Jets->at(i).eta(),Jets->at(i).phi(),isoElectronTrackHandle->at(e).eta(),isoElectronTrackHandle->at(e).phi())<JetConeSize_ ) skip=true;
            }
            for(unsigned int e=0; e<isoMuonTrackHandle->size(); ++e)
            {
               if(std::abs(Jets->at(i).pt() - isoMuonTrackHandle->at(e).pt() ) / isoMuonTrackHandle->at(e).pt() <1 && deltaR(Jets->at(i).eta(),Jets->at(i).phi(),isoMuonTrackHandle->at(e).eta(),isoMuonTrackHandle->at(e).phi())<JetConeSize_ ) skip=true;
            }
            for(unsigned int e=0; e<isoPionTrackHandle->size(); ++e)
            {
               if(std::abs(Jets->at(i).pt() - isoPionTrackHandle->at(e).pt() ) / isoPionTrackHandle->at(e).pt() <1 && deltaR(Jets->at(i).eta(),Jets->at(i).phi(),isoPionTrackHandle->at(e).eta(),isoPionTrackHandle->at(e).phi())<JetConeSize_ ) skip=true;
            }
            for(unsigned int p=0; p<photonHandle->size(); ++p)
            {
               if(std::abs(Jets->at(i).pt() - photonHandle->at(p).pt() ) / photonHandle->at(p).pt() <1 && deltaR(Jets->at(i).eta(),Jets->at(i).phi(),photonHandle->at(p).eta(),photonHandle->at(p).phi())<JetConeSize_ ) skip=true;
            }
            if(skip)
            {
               prodJets->push_back(Jet(Jets->at(i)));
		       jetsVLoose->push_back(true);
		       jetsLoose->push_back(true);
		       jetsTight->push_back(true);
		       jetsPBNR->push_back(true);
               continue;
            }
         }
         bool good = true;
         bool goodLoose = true;
         bool goodPBNR = true;
         bool goodTight = true;
         if (std::abs(Jets->at(i).eta()) < 3.0){
            good = neufrac<maxNeutralFraction_ && phofrac<maxPhotonFraction_ && nconstit>minNconstituents_;
            if(std::abs(Jets->at(i).eta()) < 2.4) good &= chgfrac>minChargedFraction_ && chgmulti>minNcharged_ && chgEMfrac<maxChargedEMFraction_;
            //other ID WPs
            goodLoose = good; //same for central jets
            goodPBNR = good && neufrac<maxNeutralFractionPBNR_ && phofrac<maxPhotonFractionPBNR_;
            goodTight = good && neufrac<maxNeutralFractionTight_ && phofrac<maxPhotonFractionTight_;
         } else {
            good = phofrac<maxPhotonFractionPBNR_ && neumulti>minNneutrals_;
            //other ID WPs
            goodLoose = good && phofrac<maxPhotonFractionHF_; //loose phofrac cut is tighter than PBNR
            goodPBNR = good && neufrac<maxNeutralFractionPBNR_ && phofrac<maxPhotonFractionPBNR_;
            goodTight = goodLoose; //same as loose for HF
         }

        //save all good jets regardless of pt
        if (good || saveAll_) {
           prodJets->push_back(Jet(Jets->at(i)));
		   jetsVLoose->push_back(good);
		   jetsLoose->push_back(goodLoose);
		   jetsTight->push_back(goodTight);
		   jetsPBNR->push_back(goodPBNR);
        } 
		//calculate event filter only for jets that pass pT cut
        if (Jets->at(i).pt() > jetPtFilter_) {
           //std::cout << "Filtered jet pT, eta: " << Jets->at(i).pt() << ", " << Jets->at(i).eta() << std::endl;
           if(!good && !TagMode_) return false;
           result &= good;
           resultLoose &= goodLoose;
           resultPBNR &= goodPBNR;
           resultTight &= goodTight;
        }
      }
   }
   // put in the event
   iEvent.put(prodJets);
   iEvent.put(jetsVLoose,"JetIDMask");
   iEvent.put(jetsLoose,"JetLooseMask");
   iEvent.put(jetsTight,"JetTightMask");
   iEvent.put(jetsPBNR,"JetPBNRMask");
   std::auto_ptr<bool> passing(new bool(result));
   iEvent.put(passing,"JetID");
   std::auto_ptr<bool> passingLoose(new bool(resultLoose));
   iEvent.put(passingLoose,"Loose");
   std::auto_ptr<bool> passingPBNR(new bool(resultPBNR));
   iEvent.put(passingPBNR,"PBNR");
   std::auto_ptr<bool> passingTight(new bool(resultTight));
   iEvent.put(passingTight,"Tight");
   return true;
   
}

// ------------ method called once each job just before starting event loop  ------------
void
GoodJetsProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
GoodJetsProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
void
GoodJetsProducer::beginRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
GoodJetsProducer::endRun(edm::Run&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
GoodJetsProducer::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
GoodJetsProducer::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GoodJetsProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
   //The following says we do not know what parameters are allowed so do no validation
   // Please change this to state exactly what you do use, even if it is no parameters
   edm::ParameterSetDescription desc;
   desc.setUnknown();
   descriptions.addDefault(desc);
}
double GoodJetsProducer::deltaR(double eta1, double phi1, double eta2, double phi2)
{
   double deta = eta1-eta2;
   double dphi = TVector2::Phi_mpi_pi(phi1-phi2);
   return sqrt(deta * deta + dphi *dphi); 
}

//define this as a plug-in
DEFINE_FWK_MODULE(GoodJetsProducer);
