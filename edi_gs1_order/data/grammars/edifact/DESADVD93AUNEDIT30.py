from bots.botsconfig import *
from recordsD93A import recorddefs
from edifact import syntax

structure=    [
{ID:'UNH',MIN:1,MAX:1,LEVEL:[
{ID:'BGM',MIN:1,MAX:1},	
{ID:'DTM',MIN:0,MAX:10},	
{ID:'RFF',MIN:0,MAX:10,LEVEL:[
    {ID:'DTM',MIN:0,MAX:1},
    ]},
{ID:'NAD',MIN:0,MAX:10,LEVEL:[	
    {ID:'RFF',MIN:0,MAX:10},	
    {ID:'CTA',MIN:0,MAX:10,LEVEL:[	
        {ID:'COM',MIN:0,MAX:5},
        ]},
    ]},
{ID:'TOD',MIN:0,MAX:10,LEVEL:[	
    {ID:'LOC',MIN:0,MAX:5},	
    ]},
{ID:'TDT',MIN:0,MAX:10,LEVEL:[	
    {ID:'LOC',MIN:0,MAX:10},	
    ]},
{ID:'EQD',MIN:0,MAX:10,LEVEL:[	
    {ID:'MEA',MIN:0,MAX:5},	
    {ID:'SEL',MIN:0,MAX:25},	
    ]},
{ID:'CPS',MIN:0,MAX:9999,LEVEL:[	
    {ID:'PAC',MIN:0,MAX:9999,LEVEL:[	
        {ID:'MEA',MIN:0,MAX:10},	
        {ID:'QTY',MIN:0,MAX:10},	
        {ID:'HAN',MIN:0,MAX:10},	
        {ID:'PCI',MIN:0,MAX:1000,LEVEL:[	
            {ID:'RFF',MIN:0,MAX:1},	
            {ID:'DTM',MIN:0,MAX:5},	
            {ID:'GIN',MIN:0,MAX:10},
            ]},
        ]},    
    {ID:'LIN',MIN:0,MAX:9999,LEVEL:[	
        {ID:'PIA',MIN:0,MAX:10},	
        {ID:'IMD',MIN:0,MAX:25},	
        {ID:'MEA',MIN:0,MAX:10},	
        {ID:'QTY',MIN:0,MAX:10},	
        {ID:'DLM',MIN:0,MAX:100},	
        {ID:'FTX',MIN:0,MAX:5},	
        {ID:'RFF',MIN:0,MAX:10,LEVEL:[	
            {ID:'DTM',MIN:0,MAX:1},	
            ]},
        {ID:'LOC',MIN:0,MAX:100,LEVEL:[	
            {ID:'DTM',MIN:0,MAX:1},	
            {ID:'QTY',MIN:0,MAX:10},	
            ]},
        {ID:'PCI',MIN:0,MAX:9999,LEVEL:[	
            {ID:'DTM',MIN:0,MAX:5},	
            {ID:'MEA',MIN:0,MAX:10},	
            {ID:'QTY',MIN:0,MAX:1},	
            {ID:'GIN',MIN:0,MAX:10,LEVEL:[	
                {ID:'DLM',MIN:0,MAX:100},	
                ]},
            {ID:'HAN',MIN:0,MAX:10},
            ]},
        {ID:'QVA',MIN:0,MAX:10,LEVEL:[	
            {ID:'DTM',MIN:0,MAX:5},	
            ]},
        ]},
    ]},
{ID:'CNT',MIN:0,MAX:5},	
{ID:'UNT',MIN:1,MAX:1},	
]
}
]
