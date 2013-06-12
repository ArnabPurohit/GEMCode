from ROOT import TH1F, TTree, TString, TCut, TGraphAsymmErrors
from ROOT import kBlue,TColor

def draw_eff(t,title, h_name, h_bins, to_draw, denom_cut, extra_num_cut, opt="", color = kBlue, marker_st = 20):
    t.Draw(to_draw + ">>num_" + h_name + h_bins, TCut("%s && %s" %(denom_cut.GetTitle(), extra_num_cut.GetTitle())), "goff")
    eff = TH1F(gDirectory.Get("num_" + h_name).Clone("eff_" + h_name))
    t.Draw(to_draw + ">>denom_" + h_name + h_bins, denom_cut, "goff")
    den = TH1F(gDirectory.Get("denom_" + h_name).Clone("denom_" + h_name))

    eff = TGraphAsymmErrors(num, den)
    eff.SetStats(0)
    eff.SetTitle(title)
    eff.SetLineWidth(2)
    eff.SetLineColor(color)
    eff.Divide(eff,den,1,1,"b")
    eff.Draw(opt)
    eff.SetMarkerStyle(marker_st)
    eff.SetMarkerColor(color)
    eff.SetMarkerSize(1.)
    return eff

def draw_geff(t, title, h_name, h_bins, to_draw, denom_cut, extra_num_cut, opt = "", color = kBlue, marker_st = 1, marker_sz = 1.):
   t.Draw(to_draw + ">>num_" + h_name + h_bins, TCut("%s && %s" %(denom_cut.GetTitle(), extra_num_cut.GetTitle())), "goff")
   num = TH1F(gDirectory.Get("num_" + h_name).Clone("eff_" + h_name))
   t.Draw(to_draw + ">>denom_" + h_name + h_bins, denom_cut, "goff")
   den = TH1F(gDirectory.Get("denom_" + h_name).Clone("denom_" + h_name))
  
   eff = TGraphAsymmErrors(num, den)
   if not "same" in opt:
       num.Reset()
       num.GetYaxis().SetRangeUser(0.,1.05)
       num.SetStats(0)
       num.SetTitle(title)
       num.Draw()
   eff.SetLineWidth(2)
   eff.SetLineColor(color)
   eff.Draw(opt + " same")
   eff.SetMarkerStyle(marker_st)
   eff.SetMarkerColor(color)
   eff.SetMarkerSize(marker_sz)
   return eff


    
