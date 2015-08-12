from pyoptics import *
from matplotlib.pyplot import *
from numpy import *

def mkfig(fn):
    ynn='g1 g2 g3'.split()
    t=optics.open(fn)
    figure(fn,figsize=(12,8))
    title(fn.split('.')[0])
    clf()
    subplot(221)
    plot(t.betx_mcby_ref,t.bety_mcby_ref,'-o')
    xlabel(r'$\beta_x \rm mcby [m]$')
    ylabel(r'$\beta_y \rm mcby [m]$')
    subplot(222)
    for yy in ynn:
        plot(t.betx_mcby_ref,abs(t[yy]),'-o',label=yy)
    xlabel(r'$\beta_x \rm mcby [m]$')
    ylabel('g [T/m]')
    ylim(128,133)
    legend()
    subplot(223)
    for yy in ynn:
        plot(t.bety_mcby_ref,abs(t[yy]),'-o',label=yy)
    xlabel(r'$\beta_y \rm mcby [m]$')
    ylabel('g [T/m]')
    ylim(128,133)
    legend()
    subplot(224)
    for yy in ynn:
        hist(abs(t[yy]),label=yy,alpha=0.2)
    xlim(128,133)
    xlabel('g [T/m]')
    legend()
    tight_layout()
    figname=fn.replace('tfs','png')
    savefig(figname)
    #os.system('cp %s  ~/dfshome/Desktop/'%figname)
def plot_range(t,lpar):
  pmax=max([max(t[ll]) for ll in lpar])
  pmin=min([min(t[ll]) for ll in lpar])
  return (pmin-20,pmax+20)
def mkfig_crab_wire(fn):
    t=optics.open(fn)
    figure('cc_'+fn,figsize=(12,8))
    title(fn.split('.')[0])
    clf()
    subplot(221)
    plot(t.betx_acfarb2_ref,t.bety_acfarb2_ref,'-o',label='ACFA')
    xlabel(r'$\beta_x \rm cc [m]$')
    ylabel(r'$\beta_y \rm cc [m]$')
#    ylim(1000,1300)
    legend()
    subplot(222)
    plot(t.betx_acfdrb2_ref,t.bety_acfdrb2_ref,'-o',label='ACFD')
    xlabel(r'$\beta_x \rm cc [m]$')
    ylabel(r'$\beta_y \rm cc [m]$')
#    ylim(900,1000)
    legend()
    subplot(223)
    plot(t.betx_wire3mlb1_ref,t.bety_wire3mlb1_ref,'-o',label='Wire 3m LB1')
    plot(t.betx_wire3mrb2_ref,t.bety_wire3mrb2_ref,'-o',label='Wire 3m RB2')
    plot(t.betx_wire5mlb1_ref,t.bety_wire5mlb1_ref,'-o',label='Wire 5m LB1')
    plot(t.betx_wire5mrb2_ref,t.bety_wire5mrb2_ref,'-o',label='Wire 5m RB2')
    plot(arange(400,1200,100),0.5*arange(400,1200,100),'-k')
    xlabel(r'$\beta_x \rm wire [m]$')
    ylabel(r'$\beta_y \rm wire [m]$')
    xlim(plot_range(t,['betx_wire3mlb1_ref','betx_wire5mlb1_ref','betx_wire3mrb2_ref','betx_wire5mrb2_ref']))
    ylim(plot_range(t,['bety_wire3mlb1_ref','bety_wire5mlb1_ref','bety_wire3mrb2_ref','bety_wire5mrb2_ref']))
    legend()
    subplot(224)
    plot(t.betx_wire3mrb1_ref,t.bety_wire3mrb1_ref,'-o',label='Wire 3m RB1')
    plot(t.betx_wire3mlb2_ref,t.bety_wire3mlb2_ref,'-o',label='Wire 3m LB2')
    plot(t.betx_wire5mrb1_ref,t.bety_wire5mrb1_ref,'-o',label='Wire 5m RB1')
    plot(t.betx_wire5mlb2_ref,t.bety_wire5mlb2_ref,'-o',label='Wire 5m LB2')
    plot(arange(400,1200,100),2*arange(400,1200,100),'-k')
    xlabel(r'$\beta_x \rm wire [m]$')
    ylabel(r'$\beta_y \rm wire [m]$')
    xlim(plot_range(t,['betx_wire3mlb2_ref','betx_wire5mlb2_ref','betx_wire3mrb1_ref','betx_wire5mrb1_ref']))
    ylim(plot_range(t,['bety_wire3mlb2_ref','bety_wire5mlb2_ref','bety_wire3mrb1_ref','bety_wire5mrb1_ref']))
    legend()
    tight_layout()
    figname=('cc_'+fn).replace('tfs','png')
    savefig(figname)
    #os.system('cp %s  ~/dfshome/Desktop/'%figname)
close('all')
mkfig('results_riccardo/presqueze_q4_scan99.3.tfs')
mkfig('results_riccardo/presqueze_q4_scan100.tfs')
mkfig('results_riccardo/presqueze_q4_scan107.tfs')
mkfig('presqueze_q4_scan99.3.tfs')
mkfig('presqueze_q4_scan100.tfs')
mkfig('presqueze_q4_scan107.tfs')
mkfig_crab_wire('presqueze_q4_scan99.3.tfs')
mkfig_crab_wire('presqueze_q4_scan100.tfs')
mkfig_crab_wire('presqueze_q4_scan107.tfs')

draw()
show()



