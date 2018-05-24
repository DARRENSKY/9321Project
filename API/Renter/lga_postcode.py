lga_list=["Ashfield","Botany Bay","Lane Cove","Leichhardt","Marrickville","Mosman","North Sydney","Randwick","Sydney","Waverley",
          "Woollahra","Auburn","Bankstown","Burwood","Canterbury","Canada Bay","Hunters Hill","Hurstville","Kogarah","Ku-Ring-Gai","Manly"
          ,"Parramatta","Rockdale","Ryde","Strathfield","Willoughby","The Hills Shire","Blacktown","Blue Mountains","Camden","Campbelltown"
          ,"Fairfield","Gosford","Hawkesbury","Holroyd","Hornsby","Liverpool","Penrith","Pittwater","Sutherland Shire","Warringah"
          ,"Wollondilly","Wyong","Cessnock","Kiama","Lake Macquarie","Maitland","Newcastle","Port Stephens","Shellharbour","Wollongong","NSW"]
postdic={2640: ['Albury', 'Corowa Shire', 'Greater Hume Shire'], 2641: ['Albury', 'Greater Hume Shire'], 2642: ['Albury', 'Corowa Shire', 'Greater Hume Shire', 'Jerilderie', 'Lockhart', 'Tumbarumba', 'Urana', 'Wagga Wagga'], 2644: ['Albury', 'Greater Hume Shire', 'Tumbarumba', 'Wagga Wagga'], 3690: ['Albury'], 3691: ['Albury', 'Greater Hume Shire'], 2350: ['Armidale Dumaresq', 'Bellingen', 'Clarence Valley', 'Glen Innes Severn', 'Guyra', 'Kempsey', 'Nambucca', 'Uralla', 'Walcha'], 2351: ['Armidale Dumaresq'], 2354: ['Armidale Dumaresq', 'Gloucester', 'Greater Taree', 'Kempsey', 'Port Macquarie-Hastings', 'Tamworth Regional', 'Upper Hunter Shire', 'Uralla', 'Walcha'], 2358: ['Armidale Dumaresq', 'Guyra', 'Tamworth Regional', 'Uralla', 'Walcha'], 2365: ['Armidale Dumaresq', 'Clarence Valley', 'Glen Innes Severn', 'Guyra', 'Inverell'], 2440: ['Armidale Dumaresq', 'Kempsey', 'Nambucca', 'Port Macquarie-Hastings', 'Walcha'], 2453: ['Armidale Dumaresq', 'Bellingen', 'Clarence Valley', 'Coffs Harbour', 'Guyra'], 2454: ['Armidale Dumaresq', 'Bellingen', 'Clarence Valley', 'Coffs Harbour', 'Kempsey', 'Nambucca'], 2040: ['Ashfield', 'Leichhardt', 'Marrickville'], 2045: ['Ashfield', 'Canada Bay', 'Leichhardt'], 2046: ['Ashfield', 'Burwood', 'Canada Bay'], 2049: ['Ashfield', 'Leichhardt', 'Marrickville'], 2130: ['Ashfield', 'Marrickville'], 2131: ['Ashfield', 'Canada Bay', 'Canterbury', 'Marrickville'], 2132: ['Ashfield', 'Burwood', 'Canada Bay'], 2133: ['Ashfield', 'Burwood', 'Canterbury', 'Strathfield'], 2193: ['Ashfield', 'Canterbury', 'Marrickville'], 2203: ['Ashfield', 'Canterbury', 'Marrickville'], 2127: ['Auburn', 'Canada Bay', 'Strathfield'], 2128: ['Auburn', 'Parramatta'], 2135: ['Auburn', 'Burwood', 'Canada Bay', 'Strathfield'], 2138: ['Auburn', 'Canada Bay', 'Strathfield'], 2140: ['Auburn', 'Canada Bay', 'Strathfield'], 2141: ['Auburn', 'Bankstown', 'Strathfield'], 2142: ['Auburn', 'Holroyd', 'Parramatta'], 2143: ['Auburn', 'Bankstown'], 2144: ['Auburn', 'Bankstown', 'Parramatta'], 2162: ['Auburn', 'Bankstown', 'Fairfield', 'Parramatta'], 2190: ['Auburn', 'Bankstown', 'Canterbury', 'Strathfield'], 2471: ['Ballina', 'Lismore', 'Richmond Valley'], 2472: ['Ballina', 'Clarence Valley', 'Lismore', 'Richmond Valley'], 2477: ['Ballina', 'Lismore', 'Richmond Valley'], 2478: ['Ballina', 'Byron', 'Lismore', 'Richmond Valley'], 2479: ['Ballina', 'Byron'], 2480: ['Ballina', 'Byron', 'Kyogle', 'Lismore', 'Richmond Valley', 'Tweed'], 2481: ['Ballina', 'Byron'], 2648: ['Balranald', 'Central Darling', 'Wentworth'], 2711: ['Balranald', 'Carrathool', 'Central Darling', 'Conargo', 'Griffith', 'Hay', 'Murrumbidgee', 'Wakool'], 2715: ['Balranald', 'Carrathool', 'Central Darling', 'Hay', 'Wakool', 'Wentworth'], 2736: ['Balranald', 'Wakool'], 2737: ['Balranald', 'Wentworth'], 2879: ['Balranald', 'Carrathool', 'Central Darling', 'Cobar', 'Wentworth'], 3501: ['Balranald', 'Wentworth'], 3549: ['Balranald'], 3597: ['Balranald', 'Wakool'], 2136: ['Bankstown', 'Burwood', 'Canterbury', 'Strathfield'], 2161: ['Bankstown', 'Fairfield', 'Holroyd', 'Parramatta'], 2163: ['Bankstown', 'Fairfield'], 2165: ['Bankstown', 'Fairfield', 'Holroyd'], 2166: ['Bankstown', 'Fairfield', 'Liverpool'], 2170: ['Bankstown', 'Campbelltown', 'Fairfield', 'Liverpool'], 2172: ['Bankstown', 'Liverpool', 'Sutherland Shire'], 2195: ['Bankstown', 'Canterbury', 'Strathfield'], 2196: ['Bankstown', 'Canterbury'], 2197: ['Bankstown'], 2198: ['Bankstown', 'Fairfield', 'Liverpool'], 2199: ['Bankstown'], 2200: ['Bankstown', 'Canterbury', 'Liverpool'], 2210: ['Bankstown', 'Canterbury', 'Hurstville'], 2211: ['Bankstown', 'Canterbury'], 2212: ['Bankstown'], 2213: ['Bankstown', 'Liverpool', 'Sutherland Shire'], 2214: ['Bankstown', 'Liverpool'], 2234: ['Bankstown', 'Liverpool', 'Sutherland Shire'], 2583: ['Bathurst Regional', 'Boorowa', 'Cowra', 'Oberon', 'Upper Lachlan Shire'], 2787: ['Bathurst Regional', 'Blue Mountains', 'Lithgow', 'Oberon', 'Penrith', 'Upper Lachlan Shire', 'Wingecarribee', 'Wollondilly'], 2795: ['Bathurst Regional', 'Blayney', 'Cabonne', 'Cowra', 'Lithgow', 'Mid-Western Regional', 'Oberon', 'Upper Lachlan Shire'], 2799: ['Bathurst Regional', 'Blayney', 'Cabonne', 'Cowra'], 2800: ['Bathurst Regional', 'Blayney', 'Cabonne', 'Cowra', 'Mid-Western Regional', 'Orange', 'Wellington'], 2808: ['Bathurst Regional', 'Blayney', 'Boorowa', 'Cowra', 'Upper Lachlan Shire'], 2846: ['Bathurst Regional', 'Lithgow', 'Mid-Western Regional'], 2847: ['Bathurst Regional', 'Lithgow'], 2850: ['Bathurst Regional', 'Cabonne', 'Lithgow', 'Mid-Western Regional', 'Upper Hunter Shire', 'Warrumbungle Shire', 'Wellington'], 2545: ['Bega Valley', 'Bombala', 'Cooma-Monaro', 'Eurobodalla', 'Palerang'], 2546: ['Bega Valley', 'Eurobodalla'], 2548: ['Bega Valley'], 2549: ['Bega Valley'], 2550: ['Bega Valley', 'Bombala'], 2551: ['Bega Valley', 'Bombala'], 2630: ['Bega Valley', 'Cooma-Monaro', 'Eurobodalla', 'Palerang', 'Snowy River'], 2631: ['Bega Valley', 'Bombala', 'Cooma-Monaro', 'Snowy River'], 2632: ['Bega Valley', 'Bombala', 'Cooma-Monaro', 'Snowy River'], 3889: ['Bega Valley', 'Bombala'], 3891: ['Bega Valley'], 2441: ['Bellingen', 'Coffs Harbour', 'Kempsey', 'Nambucca', 'Port Macquarie-Hastings'], 2448: ['Bellingen', 'Nambucca'], 2449: ['Bellingen', 'Kempsey', 'Nambucca'], 2450: ['Bellingen', 'Clarence Valley', 'Coffs Harbour'], 2455: ['Bellingen', 'Nambucca'], 2646: ['Berrigan', 'Corowa Shire', 'Greater Hume Shire', 'Jerilderie', 'Urana'], 2710: ['Berrigan', 'Conargo', 'Deniliquin', 'Hay', 'Jerilderie', 'Murray', 'Murrumbidgee', 'Wakool'], 2712: ['Berrigan', 'Corowa Shire', 'Jerilderie'], 2713: ['Berrigan', 'Conargo', 'Corowa Shire', 'Jerilderie', 'Murray', 'Urana'], 2714: ['Berrigan', 'Conargo', 'Murray'], 3641: ['Berrigan', 'Murray'], 3644: ['Berrigan'], 3730: ['Berrigan', 'Corowa Shire'], 2145: ['Blacktown', 'Fairfield', 'Holroyd', 'Parramatta'], 2146: ['Blacktown', 'Holroyd', 'Parramatta'], 2147: ['Blacktown', 'Parramatta', 'The Hills Shire'], 2148: ['Blacktown', 'Holroyd'], 2153: ['Blacktown', 'Parramatta', 'The Hills Shire'], 2155: ['Blacktown', 'The Hills Shire'], 2164: ['Blacktown', 'Fairfield', 'Holroyd'], 2175: ['Blacktown', 'Fairfield', 'Penrith'], 2178: ['Blacktown', 'Fairfield', 'Liverpool', 'Penrith'], 2747: ['Blacktown', 'Penrith'], 2756: ['Blacktown', 'Blue Mountains', 'Cessnock', 'Hawkesbury', 'Hornsby', 'Lithgow', 'Penrith', 'Singleton', 'The Hills Shire'], 2759: ['Blacktown', 'Penrith'], 2760: ['Blacktown', 'Penrith'], 2761: ['Blacktown'], 2762: ['Blacktown'], 2763: ['Blacktown'], 2765: ['Blacktown', 'Hawkesbury', 'Penrith', 'The Hills Shire'], 2766: ['Blacktown', 'Fairfield', 'Holroyd', 'Penrith'], 2767: ['Blacktown'], 2768: ['Blacktown', 'The Hills Shire'], 2769: ['Blacktown'], 2770: ['Blacktown', 'Penrith'], 2594: ['Bland', 'Cootamundra', 'Harden', 'Temora', 'Weddin', 'Young'], 2665: ['Bland', 'Carrathool', 'Coolamon', 'Griffith', 'Junee', 'Leeton', 'Narrandera', 'Temora'], 2666: ['Bland', 'Cootamundra', 'Junee', 'Temora', 'Young'], 2668: ['Bland', 'Temora'], 2669: ['Bland', 'Carrathool', 'Coolamon', 'Griffith', 'Lachlan', 'Narrandera'], 2671: ['Bland', 'Forbes', 'Lachlan', 'Temora', 'Weddin', 'Young'], 2672: ['Bland', 'Carrathool', 'Cobar', 'Lachlan'], 2675: ['Bland', 'Carrathool', 'Central Darling', 'Cobar', 'Lachlan'], 2721: ['Bland', 'Weddin', 'Young'], 2810: ['Bland', 'Cowra', 'Forbes', 'Weddin', 'Young'], 2871: ['Bland', 'Cabonne', 'Cowra', 'Forbes', 'Lachlan', 'Parkes', 'Weddin'], 2877: ['Bland', 'Bogan', 'Carrathool', 'Cobar', 'Forbes', 'Lachlan'], 2791: ['Blayney', 'Cabonne', 'Cowra'], 2792: ['Blayney', 'Cowra'], 2793: ['Blayney', 'Boorowa', 'Cowra'], 2797: ['Blayney'], 2798: ['Blayney', 'Cabonne', 'Orange'], 2804: ['Blayney', 'Cabonne', 'Cowra', 'Forbes'], 2745: ['Blue Mountains', 'Camden', 'Liverpool', 'Penrith', 'Wollondilly'], 2749: ['Blue Mountains', 'Hawkesbury', 'Penrith'], 2750: ['Blue Mountains', 'Penrith'], 2753: ['Blue Mountains', 'Hawkesbury', 'Penrith'], 2758: ['Blue Mountains', 'Hawkesbury', 'Lithgow'], 2773: ['Blue Mountains', 'Penrith'], 2774: ['Blue Mountains', 'Penrith'], 2776: ['Blue Mountains'], 2777: ['Blue Mountains', 'Hawkesbury', 'Penrith'], 2778: ['Blue Mountains'], 2779: ['Blue Mountains'], 2780: ['Blue Mountains'], 2782: ['Blue Mountains'], 2783: ['Blue Mountains'], 2784: ['Blue Mountains'], 2785: ['Blue Mountains', 'Lithgow', 'Oberon'], 2786: ['Blue Mountains', 'Lithgow'], 2790: ['Blue Mountains', 'Lithgow', 'Oberon'], 2849: ['Blue Mountains', 'Hawkesbury', 'Lithgow', 'Mid-Western Regional', 'Muswellbrook', 'Singleton', 'Upper Hunter Shire'], 2824: ['Bogan', 'Brewarrina', 'Coonamble', 'Warren'], 2825: ['Bogan', 'Cobar', 'Lachlan', 'Warren'], 2831: ['Bogan', 'Brewarrina', 'Cobar', 'Coonamble', 'Dubbo', 'Gilgandra', 'Lachlan', 'Narromine', 'Walgett', 'Warren', 'Warrumbungle Shire', 'Wellington'], 2835: ['Bogan', 'Bourke', 'Central Darling', 'Cobar'], 2839: ['Bogan', 'Bourke', 'Brewarrina', 'Cobar', 'Walgett', 'Warren'], 2840: ['Bogan', 'Bourke', 'Brewarrina', 'Central Darling', 'Cobar'], 2873: ['Bogan', 'Lachlan', 'Narromine', 'Parkes', 'Warren'], 2627: ['Bombala', 'Cooma-Monaro', 'Snowy River', 'Tumbarumba', 'Tumut Shire'], 2633: ['Bombala', 'Snowy River'], 3888: ['Bombala', 'Snowy River'], 2581: ['Boorowa', 'Goulburn Mulwaree', 'Palerang', 'Upper Lachlan Shire', 'Yass Valley'], 2582: ['Boorowa', 'Gundagai', 'Harden', 'Tumut Shire', 'Upper Lachlan Shire', 'Yass Valley'], 2584: ['Boorowa', 'Harden', 'Yass Valley'], 2585: ['Boorowa', 'Harden', 'Yass Valley', 'Young'], 2586: ['Boorowa', 'Cowra', 'Harden', 'Upper Lachlan Shire', 'Yass Valley', 'Young'], 2794: ['Boorowa', 'Cowra', 'Weddin', 'Young'], 2803: ['Boorowa', 'Cowra', 'Weddin', 'Young'], 2015: ['Botany Bay', 'Marrickville', 'Sydney'], 2018: ['Botany Bay', 'Randwick', 'Sydney'], 2019: ['Botany Bay', 'Randwick'], 2020: ['Botany Bay', 'Marrickville', 'Rockdale', 'Sydney'], 2032: ['Botany Bay', 'Randwick'], 2033: ['Botany Bay', 'Randwick', 'Sydney'], 2035: ['Botany Bay', 'Randwick'], 2036: ['Botany Bay', 'Randwick'], 2044: ['Botany Bay', 'Marrickville', 'Rockdale', 'Sydney'], 2836: ['Bourke', 'Central Darling', 'Cobar'], 2880: ['Bourke', 'Broken Hill', 'Central Darling', 'Wentworth'], 4490: ['Bourke', 'Brewarrina'], 4492: ['Bourke'], 2832: ['Brewarrina', 'Coonamble', 'Narrabri', 'Walgett'], 2834: ['Brewarrina', 'Walgett'], 4488: ['Brewarrina'], 2134: ['Burwood', 'Canada Bay'], 2137: ['Burwood', 'Canada Bay', 'Strathfield'], 2191: ['Burwood', 'Canterbury', 'Strathfield'], 2194: ['Burwood', 'Canterbury'], 2482: ['Byron', 'Lismore', 'Tweed'], 2483: ['Byron', 'Tweed'], 2484: ['Byron', 'Kyogle', 'Lismore', 'Tweed'], 2805: ['Cabonne', 'Cowra', 'Forbes', 'Weddin'], 2806: ['Cabonne', 'Forbes', 'Parkes'], 2820: ['Cabonne', 'Dubbo', 'Mid-Western Regional', 'Warrumbungle Shire', 'Wellington'], 2830: ['Cabonne', 'Dubbo', 'Gilgandra', 'Narromine', 'Parkes', 'Warrumbungle Shire', 'Wellington'], 2864: ['Cabonne'], 2865: ['Cabonne', 'Parkes'], 2866: ['Cabonne', 'Parkes', 'Wellington'], 2867: ['Cabonne', 'Parkes', 'Wellington'], 2868: ['Cabonne', 'Dubbo', 'Wellington'], 2869: ['Cabonne', 'Dubbo', 'Narromine', 'Parkes'], 2870: ['Cabonne', 'Forbes', 'Parkes'], 2171: ['Camden', 'Fairfield', 'Liverpool'], 2179: ['Camden', 'Campbelltown', 'Liverpool'], 2556: ['Camden', 'Liverpool'], 2557: ['Camden', 'Campbelltown', 'Liverpool'], 2558: ['Camden', 'Campbelltown'], 2559: ['Camden', 'Campbelltown'], 2560: ['Camden', 'Campbelltown', 'Wollondilly', 'Wollongong'], 2565: ['Camden', 'Campbelltown', 'Liverpool'], 2566: ['Camden', 'Campbelltown', 'Liverpool'], 2567: ['Camden', 'Campbelltown', 'Wollondilly'], 2569: ['Camden', 'Campbelltown', 'Wollondilly'], 2570: ['Camden', 'Liverpool', 'Wollondilly'], 2167: ['Campbelltown', 'Liverpool'], 2173: ['Campbelltown', 'Liverpool', 'Sutherland Shire', 'Wollondilly', 'Wollongong'], 2508: ['Campbelltown', 'Sutherland Shire', 'Wollondilly', 'Wollongong'], 2563: ['Campbelltown', 'Wollondilly'], 2564: ['Campbelltown', 'Liverpool'], 2047: ['Canada Bay'], 2139: ['Canada Bay'], 2192: ['Canterbury', 'Strathfield'], 2204: ['Canterbury', 'Marrickville', 'Rockdale'], 2205: ['Canterbury', 'Marrickville', 'Rockdale'], 2206: ['Canterbury', 'Marrickville', 'Rockdale'], 2207: ['Canterbury', 'Hurstville', 'Rockdale'], 2208: ['Canterbury', 'Hurstville', 'Rockdale'], 2209: ['Canterbury', 'Hurstville'], 2652: ['Carrathool', 'Coolamon', 'Greater Hume Shire', 'Gundagai', 'Hay', 'Jerilderie', 'Junee', 'Leeton', 'Lockhart', 'Murrumbidgee', 'Narrandera', 'Temora', 'Tumbarumba', 'Tumut Shire', 'Urana', 'Wagga Wagga'], 2680: ['Carrathool', 'Griffith', 'Leeton', 'Murrumbidgee'], 2681: ['Carrathool', 'Griffith'], 2707: ['Carrathool', 'Conargo', 'Griffith', 'Hay', 'Jerilderie', 'Murrumbidgee', 'Narrandera', 'Urana'], 2878: ['Central Darling'], 2250: ['Cessnock', 'Gosford', 'Hawkesbury', 'Wyong'], 2259: ['Cessnock', 'Lake Macquarie', 'Wyong'], 2265: ['Cessnock', 'Lake Macquarie', 'Wyong'], 2278: ['Cessnock', 'Lake Macquarie'], 2286: ['Cessnock', 'Lake Macquarie'], 2287: ['Cessnock', 'Lake Macquarie', 'Newcastle'], 2320: ['Cessnock', 'Dungog', 'Maitland', 'Port Stephens', 'Singleton'], 2321: ['Cessnock', 'Dungog', 'Great Lakes', 'Maitland', 'Port Stephens', 'Singleton'], 2322: ['Cessnock', 'Maitland', 'Newcastle', 'Port Stephens'], 2323: ['Cessnock', 'Lake Macquarie', 'Maitland', 'Newcastle'], 2325: ['Cessnock', 'Gosford', 'Hawkesbury', 'Lake Macquarie', 'Maitland', 'Singleton', 'Wyong'], 2326: ['Cessnock', 'Maitland'], 2327: ['Cessnock'], 2330: ['Cessnock', 'Dungog', 'Hawkesbury', 'Muswellbrook', 'Singleton', 'Upper Hunter Shire'], 2334: ['Cessnock', 'Maitland', 'Singleton'], 2335: ['Cessnock', 'Dungog', 'Maitland', 'Singleton'], 2775: ['Cessnock', 'Gosford', 'Hawkesbury', 'Hornsby', 'The Hills Shire'], 2370: ['Clarence Valley', 'Glen Innes Severn', 'Inverell', 'Tenterfield'], 2456: ['Clarence Valley', 'Coffs Harbour'], 2460: ['Clarence Valley', 'Coffs Harbour', 'Glen Innes Severn', 'Guyra', 'Richmond Valley'], 2462: ['Clarence Valley'], 2463: ['Clarence Valley', 'Richmond Valley'], 2464: ['Clarence Valley'], 2465: ['Clarence Valley'], 2466: ['Clarence Valley'], 2469: ['Clarence Valley', 'Glen Innes Severn', 'Kyogle', 'Richmond Valley', 'Tenterfield'], 2452: ['Coffs Harbour'], 2716: ['Conargo', 'Jerilderie', 'Murrumbidgee', 'Urana'], 2732: ['Conargo', 'Murray', 'Wakool'], 2733: ['Conargo', 'Hay', 'Wakool'], 2650: ['Coolamon', 'Greater Hume Shire', 'Gundagai', 'Junee', 'Lockhart', 'Narrandera', 'Wagga Wagga'], 2701: ['Coolamon', 'Junee', 'Temora', 'Wagga Wagga'], 2702: ['Coolamon'], 2620: ['Cooma-Monaro', 'Palerang', 'Queanbeyan', 'Tumut Shire', 'Upper Lachlan Shire', 'Yass Valley'], 2621: ['Cooma-Monaro', 'Palerang', 'Queanbeyan', 'Yass Valley'], 2622: ['Cooma-Monaro', 'Eurobodalla', 'Goulburn Mulwaree', 'Palerang', 'Shoalhaven', 'Wingecarribee'], 2623: ['Cooma-Monaro', 'Palerang'], 2626: ['Cooma-Monaro'], 2628: ['Cooma-Monaro', 'Snowy River', 'Tumbarumba'], 2629: ['Cooma-Monaro', 'Snowy River'], 2720: ['Cooma-Monaro', 'Gundagai', 'Snowy River', 'Tumbarumba', 'Tumut Shire', 'Yass Valley'], 2900: ['Cooma-Monaro', 'Palerang', 'Queanbeyan'], 2357: ['Coonamble', 'Gilgandra', 'Gunnedah', 'Liverpool Plains', 'Narrabri', 'Warrumbungle Shire'], 2388: ['Coonamble', 'Gunnedah', 'Moree Plains', 'Narrabri', 'Walgett', 'Warrumbungle Shire'], 2396: ['Coonamble', 'Gilgandra', 'Narrabri', 'Warrumbungle Shire'], 2827: ['Coonamble', 'Dubbo', 'Gilgandra', 'Narromine', 'Warren', 'Warrumbungle Shire'], 2828: ['Coonamble', 'Gilgandra', 'Warren'], 2829: ['Coonamble', 'Gilgandra', 'Narrabri', 'Walgett', 'Warrumbungle Shire'], 2587: ['Cootamundra', 'Harden', 'Young'], 2588: ['Cootamundra', 'Harden', 'Young'], 2590: ['Cootamundra', 'Gundagai', 'Harden', 'Junee', 'Temora'], 2725: ['Cootamundra', 'Junee', 'Temora', 'Young'], 2726: ['Cootamundra', 'Gundagai', 'Harden', 'Yass Valley'], 2727: ['Cootamundra', 'Gundagai', 'Harden', 'Junee', 'Tumut Shire', 'Yass Valley'], 2643: ['Corowa Shire', 'Greater Hume Shire'], 2647: ['Corowa Shire'], 3682: ['Corowa Shire'], 3685: ['Corowa Shire'], 3687: ['Corowa Shire'], 3688: ['Corowa Shire', 'Greater Hume Shire'], 2807: ['Cowra', 'Young'], 2809: ['Cowra', 'Weddin', 'Young'], 2821: ['Dubbo', 'Gilgandra', 'Narromine', 'Parkes'], 2842: ['Dubbo', 'Gilgandra', 'Warrumbungle Shire'], 2844: ['Dubbo', 'Mid-Western Regional', 'Upper Hunter Shire', 'Warrumbungle Shire', 'Wellington'], 2311: ['Dungog', 'Gloucester', 'Singleton', 'Upper Hunter Shire'], 2324: ['Dungog', 'Great Lakes', 'Maitland', 'Port Stephens'], 2336: ['Dungog', 'Muswellbrook', 'Singleton', 'Upper Hunter Shire'], 2337: ['Dungog', 'Gloucester', 'Liverpool Plains', 'Muswellbrook', 'Upper Hunter Shire'], 2415: ['Dungog', 'Gloucester', 'Great Lakes'], 2420: ['Dungog', 'Gloucester', 'Great Lakes', 'Port Stephens'], 2421: ['Dungog', 'Maitland', 'Port Stephens', 'Singleton'], 2422: ['Dungog', 'Gloucester', 'Greater Taree', 'Great Lakes', 'Upper Hunter Shire', 'Walcha'], 2425: ['Dungog', 'Great Lakes'], 2536: ['Eurobodalla', 'Palerang', 'Shoalhaven'], 2537: ['Eurobodalla'], 2538: ['Eurobodalla', 'Shoalhaven'], 2168: ['Fairfield', 'Liverpool'], 2176: ['Fairfield', 'Liverpool'], 2177: ['Fairfield', 'Liverpool'], 2875: ['Forbes', 'Lachlan', 'Parkes'], 2876: ['Forbes', 'Parkes'], 2395: ['Gilgandra', 'Warrumbungle Shire'], 2823: ['Gilgandra', 'Lachlan', 'Narromine', 'Parkes', 'Warren'], 2360: ['Glen Innes Severn', 'Guyra', 'Gwydir', 'Inverell', 'Tamworth Regional', 'Uralla'], 2361: ['Glen Innes Severn', 'Inverell', 'Tenterfield'], 2371: ['Glen Innes Severn', 'Tenterfield'], 2372: ['Glen Innes Severn', 'Inverell', 'Kyogle', 'Tenterfield'], 2338: ['Gloucester', 'Liverpool Plains', 'Tamworth Regional', 'Upper Hunter Shire', 'Walcha'], 2423: ['Gloucester', 'Greater Taree', 'Great Lakes'], 2424: ['Gloucester', 'Greater Taree', 'Port Macquarie-Hastings', 'Walcha'], 2429: ['Gloucester', 'Greater Taree', 'Great Lakes', 'Port Macquarie-Hastings'], 2082: ['Gosford', 'Hornsby'], 2083: ['Gosford', 'Hornsby'], 2251: ['Gosford'], 2256: ['Gosford'], 2257: ['Gosford'], 2258: ['Gosford', 'Wyong'], 2260: ['Gosford', 'Wyong'], 2261: ['Gosford', 'Wyong'], 2577: ['Goulburn Mulwaree', 'Kiama', 'Shellharbour', 'Shoalhaven', 'Upper Lachlan Shire', 'Wingecarribee'], 2579: ['Goulburn Mulwaree', 'Shoalhaven', 'Upper Lachlan Shire', 'Wingecarribee'], 2580: ['Goulburn Mulwaree', 'Oberon', 'Palerang', 'Shoalhaven', 'Upper Lachlan Shire', 'Wingecarribee', 'Wollondilly', 'Yass Valley'], 2653: ['Greater Hume Shire', 'Tumbarumba', 'Tumut Shire', 'Wagga Wagga'], 2656: ['Greater Hume Shire', 'Lockhart', 'Narrandera', 'Urana', 'Wagga Wagga'], 2658: ['Greater Hume Shire', 'Lockhart', 'Wagga Wagga'], 2659: ['Greater Hume Shire'], 2660: ['Greater Hume Shire', 'Wagga Wagga'], 3700: ['Greater Hume Shire'], 3709: ['Greater Hume Shire', 'Tumbarumba'], 2312: ['Greater Taree', 'Great Lakes'], 2426: ['Greater Taree'], 2427: ['Greater Taree'], 2428: ['Greater Taree', 'Great Lakes'], 2430: ['Greater Taree', 'Great Lakes', 'Port Macquarie-Hastings'], 2439: ['Greater Taree', 'Port Macquarie-Hastings'], 2443: ['Greater Taree', 'Port Macquarie-Hastings'], 2446: ['Greater Taree', 'Kempsey', 'Port Macquarie-Hastings', 'Walcha'], 2705: ['Griffith', 'Leeton', 'Murrumbidgee', 'Narrandera'], 2706: ['Griffith', 'Leeton', 'Murrumbidgee', 'Narrandera'], 2722: ['Gundagai', 'Junee', 'Tumut Shire', 'Yass Valley'], 2729: ['Gundagai', 'Junee', 'Tumbarumba', 'Tumut Shire', 'Wagga Wagga'], 2340: ['Gunnedah', 'Liverpool Plains', 'Tamworth Regional', 'Upper Hunter Shire'], 2341: ['Gunnedah', 'Liverpool Plains', 'Tamworth Regional'], 2342: ['Gunnedah', 'Liverpool Plains', 'Tamworth Regional'], 2343: ['Gunnedah', 'Liverpool Plains', 'Tamworth Regional', 'Upper Hunter Shire'], 2344: ['Gunnedah', 'Liverpool Plains', 'Tamworth Regional'], 2346: ['Gunnedah', 'Narrabri', 'Tamworth Regional'], 2380: ['Gunnedah', 'Narrabri', 'Tamworth Regional', 'Warrumbungle Shire'], 2381: ['Gunnedah', 'Liverpool Plains', 'Upper Hunter Shire', 'Warrumbungle Shire'], 2382: ['Gunnedah', 'Narrabri'], 2390: ['Gunnedah', 'Gwydir', 'Moree Plains', 'Narrabri', 'Tamworth Regional'], 2359: ['Guyra', 'Gwydir', 'Tamworth Regional', 'Uralla'], 2369: ['Guyra', 'Gwydir', 'Inverell', 'Uralla'], 2347: ['Gwydir', 'Moree Plains', 'Narrabri', 'Tamworth Regional', 'Uralla'], 2399: ['Gwydir', 'Moree Plains', 'Narrabri'], 2400: ['Gwydir', 'Moree Plains', 'Narrabri', 'Walgett'], 2401: ['Gwydir', 'Moree Plains'], 2402: ['Gwydir', 'Inverell'], 2403: ['Gwydir', 'Inverell'], 2404: ['Gwydir', 'Inverell', 'Moree Plains', 'Tamworth Regional'], 2408: ['Gwydir', 'Inverell', 'Moree Plains'], 2409: ['Gwydir', 'Inverell', 'Moree Plains'], 2410: ['Gwydir', 'Inverell', 'Moree Plains'], 2754: ['Hawkesbury'], 2757: ['Hawkesbury'], 2150: ['Holroyd', 'Parramatta', 'The Hills Shire'], 2160: ['Holroyd', 'Parramatta'], 2074: ['Hornsby', 'Ku-ring-gai', 'Ryde', 'Warringah'], 2076: ['Hornsby', 'Ku-ring-gai'], 2077: ['Hornsby', 'Ku-ring-gai'], 2079: ['Hornsby'], 2080: ['Hornsby', 'Ku-ring-gai'], 2081: ['Hornsby'], 2118: ['Hornsby', 'Parramatta', 'The Hills Shire'], 2119: ['Hornsby', 'The Hills Shire'], 2120: ['Hornsby', 'Ku-ring-gai'], 2121: ['Hornsby', 'Ku-ring-gai', 'Parramatta', 'Ryde'], 2122: ['Hornsby', 'Ku-ring-gai', 'Parramatta', 'Ryde'], 2125: ['Hornsby', 'The Hills Shire'], 2126: ['Hornsby', 'The Hills Shire'], 2154: ['Hornsby', 'The Hills Shire'], 2156: ['Hornsby', 'The Hills Shire'], 2157: ['Hornsby', 'The Hills Shire'], 2158: ['Hornsby', 'The Hills Shire'], 2159: ['Hornsby'], 2110: ['Hunters Hill', 'Ryde'], 2111: ['Hunters Hill', 'Ryde'], 2113: ['Hunters Hill', 'Ku-ring-gai', 'Ryde', 'Willoughby'], 2218: ['Hurstville', 'Kogarah', 'Rockdale'], 2220: ['Hurstville', 'Kogarah', 'Rockdale'], 2222: ['Hurstville', 'Kogarah'], 2223: ['Hurstville', 'Kogarah'], 4385: ['Inverell', 'Tenterfield'], 4388: ['Inverell', 'Moree Plains'], 2663: ['Junee'], 2431: ['Kempsey'], 2444: ['Kempsey', 'Port Macquarie-Hastings'], 2447: ['Kempsey', 'Nambucca'], 2527: ['Kiama', 'Shellharbour', 'Wingecarribee', 'Wollongong'], 2529: ['Kiama', 'Shellharbour'], 2533: ['Kiama', 'Shellharbour', 'Shoalhaven'], 2534: ['Kiama', 'Shoalhaven'], 2535: ['Kiama', 'Shoalhaven'], 2216: ['Kogarah', 'Rockdale'], 2217: ['Kogarah', 'Rockdale'], 2219: ['Kogarah', 'Rockdale'], 2221: ['Kogarah', 'Sutherland Shire'], 2224: ['Kogarah', 'Sutherland Shire'], 2067: ['Ku-ring-gai', 'Lane Cove', 'Ryde', 'Willoughby'], 2069: ['Ku-ring-gai', 'Warringah', 'Willoughby'], 2070: ['Ku-ring-gai', 'Ryde', 'Warringah', 'Willoughby'], 2071: ['Ku-ring-gai', 'Ryde', 'Warringah'], 2072: ['Ku-ring-gai'], 2073: ['Ku-ring-gai', 'Ryde'], 2075: ['Ku-ring-gai', 'Warringah'], 2084: ['Ku-ring-gai', 'Pittwater', 'Warringah'], 2085: ['Ku-ring-gai', 'Warringah'], 2086: ['Ku-ring-gai', 'Warringah'], 2087: ['Ku-ring-gai', 'Manly', 'Warringah'], 2470: ['Kyogle', 'Lismore', 'Richmond Valley'], 2474: ['Kyogle', 'Lismore', 'Richmond Valley', 'Tweed'], 2475: ['Kyogle', 'Tenterfield'], 2476: ['Kyogle', 'Tenterfield'], 4275: ['Kyogle', 'Tweed'], 4285: ['Kyogle'], 4287: ['Kyogle'], 4310: ['Kyogle', 'Tenterfield'], 2874: ['Lachlan', 'Narromine', 'Parkes'], 2262: ['Lake Macquarie', 'Wyong'], 2264: ['Lake Macquarie', 'Wyong'], 2267: ['Lake Macquarie'], 2280: ['Lake Macquarie'], 2281: ['Lake Macquarie', 'Wyong'], 2282: ['Lake Macquarie'], 2283: ['Lake Macquarie'], 2284: ['Lake Macquarie'], 2285: ['Lake Macquarie', 'Newcastle'], 2289: ['Lake Macquarie', 'Newcastle'], 2290: ['Lake Macquarie', 'Newcastle'], 2291: ['Lake Macquarie', 'Newcastle'], 2305: ['Lake Macquarie', 'Newcastle'], 2306: ['Lake Macquarie'], 2064: ['Lane Cove', 'Willoughby'], 2065: ['Lane Cove', 'North Sydney', 'Willoughby'], 2066: ['Lane Cove', 'Ryde', 'Willoughby'], 2700: ['Leeton', 'Lockhart', 'Murrumbidgee', 'Narrandera', 'Urana', 'Wagga Wagga'], 2703: ['Leeton'], 2037: ['Leichhardt', 'Sydney'], 2038: ['Leichhardt', 'Marrickville', 'Sydney'], 2039: ['Leichhardt'], 2041: ['Leichhardt'], 2048: ['Leichhardt', 'Marrickville'], 2050: ['Leichhardt', 'Marrickville', 'Sydney'], 2473: ['Lismore', 'Richmond Valley'], 2845: ['Lithgow'], 2848: ['Lithgow', 'Mid-Western Regional'], 2174: ['Liverpool'], 2555: ['Liverpool', 'Penrith'], 2752: ['Liverpool', 'Wollondilly'], 2329: ['Liverpool Plains', 'Mid-Western Regional', 'Muswellbrook', 'Upper Hunter Shire', 'Warrumbungle Shire'], 2339: ['Liverpool Plains', 'Upper Hunter Shire'], 2843: ['Liverpool Plains', 'Upper Hunter Shire', 'Warrumbungle Shire'], 2655: ['Lockhart', 'Wagga Wagga'], 2092: ['Manly', 'Warringah'], 2093: ['Manly', 'Warringah'], 2094: ['Manly'], 2095: ['Manly', 'Warringah'], 2096: ['Manly', 'Warringah'], 2100: ['Manly', 'Warringah'], 2042: ['Marrickville', 'Sydney'], 2043: ['Marrickville', 'Sydney'], 2328: ['Mid-Western Regional', 'Muswellbrook', 'Singleton', 'Upper Hunter Shire'], 2852: ['Mid-Western Regional', 'Warrumbungle Shire', 'Wellington'], 2397: ['Moree Plains', 'Narrabri'], 2405: ['Moree Plains'], 2406: ['Moree Plains', 'Walgett'], 2833: ['Moree Plains', 'Narrabri', 'Walgett'], 4390: ['Moree Plains'], 4494: ['Moree Plains'], 4496: ['Moree Plains'], 4497: ['Moree Plains', 'Walgett'], 4498: ['Moree Plains'], 2088: ['Mosman', 'North Sydney'], 2090: ['Mosman', 'North Sydney'], 2731: ['Murray', 'Wakool'], 3562: ['Murray'], 3564: ['Murray'], 3566: ['Murray'], 3567: ['Murray'], 3568: ['Murray', 'Wakool'], 3573: ['Murray'], 3637: ['Murray'], 3638: ['Murray'], 3639: ['Murray'], 2333: ['Muswellbrook', 'Singleton', 'Upper Hunter Shire'], 2386: ['Narrabri', 'Walgett'], 2292: ['Newcastle'], 2293: ['Newcastle'], 2294: ['Newcastle'], 2295: ['Newcastle', 'Port Stephens'], 2296: ['Newcastle'], 2297: ['Newcastle'], 2298: ['Newcastle'], 2299: ['Newcastle'], 2300: ['Newcastle'], 2302: ['Newcastle'], 2303: ['Newcastle'], 2304: ['Newcastle'], 2307: ['Newcastle'], 2308: ['Newcastle'], 2060: ['North Sydney'], 2061: ['North Sydney'], 2062: ['North Sydney', 'Willoughby'], 2063: ['North Sydney', 'Willoughby'], 2089: ['North Sydney'], 2609: ['Palerang', 'Queanbeyan'], 2912: ['Palerang', 'Yass Valley'], 2114: ['Parramatta', 'Ryde'], 2115: ['Parramatta', 'Ryde'], 2116: ['Parramatta'], 2117: ['Parramatta', 'Ryde', 'The Hills Shire'], 2151: ['Parramatta', 'The Hills Shire'], 2152: ['Parramatta', 'The Hills Shire'], 2748: ['Penrith'], 2101: ['Pittwater', 'Warringah'], 2102: ['Pittwater'], 2103: ['Pittwater'], 2104: ['Pittwater'], 2105: ['Pittwater'], 2106: ['Pittwater'], 2107: ['Pittwater'], 2108: ['Pittwater', 'Warringah'], 2445: ['Port Macquarie-Hastings'], 2314: ['Port Stephens'], 2315: ['Port Stephens'], 2316: ['Port Stephens'], 2317: ['Port Stephens'], 2318: ['Port Stephens'], 2319: ['Port Stephens'], 2600: ['Queanbeyan'], 2619: ['Queanbeyan'], 2017: ['Randwick', 'Sydney'], 2021: ['Randwick', 'Sydney', 'Waverley', 'Woollahra'], 2022: ['Randwick', 'Waverley', 'Woollahra'], 2024: ['Randwick', 'Waverley'], 2025: ['Randwick', 'Sydney', 'Waverley', 'Woollahra'], 2031: ['Randwick', 'Waverley'], 2034: ['Randwick'], 2052: ['Randwick'], 2109: ['Ryde'], 2112: ['Ryde'], 2528: ['Shellharbour', 'Wollongong'], 2530: ['Shellharbour', 'Wollongong'], 2574: ['Shellharbour', 'Wingecarribee', 'Wollondilly', 'Wollongong'], 2576: ['Shellharbour', 'Wingecarribee', 'Wollongong'], 2539: ['Shoalhaven'], 2540: ['Shoalhaven'], 2541: ['Shoalhaven'], 2625: ['Snowy River'], 2649: ['Snowy River', 'Tumbarumba', 'Tumut Shire'], 2129: ['Strathfield'], 2225: ['Sutherland Shire'], 2226: ['Sutherland Shire'], 2227: ['Sutherland Shire'], 2228: ['Sutherland Shire'], 2229: ['Sutherland Shire'], 2230: ['Sutherland Shire'], 2231: ['Sutherland Shire'], 2232: ['Sutherland Shire'], 2233: ['Sutherland Shire', 'Wollongong'], 2000: ['Sydney'], 2006: ['Sydney'], 2007: ['Sydney'], 2008: ['Sydney'], 2009: ['Sydney'], 2010: ['Sydney', 'Woollahra'], 2011: ['Sydney', 'Woollahra'], 2016: ['Sydney'], 2027: ['Sydney', 'Woollahra'], 2345: ['Tamworth Regional'], 2352: ['Tamworth Regional', 'Walcha'], 2353: ['Tamworth Regional'], 2355: ['Tamworth Regional', 'Uralla'], 4370: ['Tenterfield'], 4373: ['Tenterfield'], 4374: ['Tenterfield'], 4375: ['Tenterfield'], 4376: ['Tenterfield'], 4377: ['Tenterfield'], 4378: ['Tenterfield'], 4380: ['Tenterfield'], 4382: ['Tenterfield'], 4383: ['Tenterfield'], 2730: ['Tumbarumba', 'Tumut Shire'], 3705: ['Tumbarumba'], 3707: ['Tumbarumba'], 3885: ['Tumbarumba'], 2485: ['Tweed'], 2486: ['Tweed'], 2487: ['Tweed'], 2488: ['Tweed'], 2489: ['Tweed'], 2490: ['Tweed'], 4211: ['Tweed'], 4213: ['Tweed'], 4223: ['Tweed'], 4224: ['Tweed'], 4225: ['Tweed'], 4228: ['Tweed'], 2575: ['Upper Lachlan Shire', 'Wingecarribee', 'Wollondilly'], 2645: ['Urana'], 2651: ['Wagga Wagga'], 2661: ['Wagga Wagga'], 2678: ['Wagga Wagga'], 2735: ['Wakool'], 3579: ['Wakool'], 3580: ['Wakool'], 3585: ['Wakool'], 3586: ['Wakool'], 3590: ['Wakool'], 3591: ['Wakool'], 3594: ['Wakool'], 3596: ['Wakool'], 4486: ['Walgett'], 2097: ['Warringah'], 2099: ['Warringah'], 2023: ['Waverley', 'Woollahra'], 2026: ['Waverley', 'Woollahra'], 2029: ['Waverley', 'Woollahra'], 2030: ['Waverley', 'Woollahra'], 2717: ['Wentworth'], 2738: ['Wentworth'], 2739: ['Wentworth'], 3494: ['Wentworth'], 3496: ['Wentworth'], 3498: ['Wentworth'], 3500: ['Wentworth'], 3505: ['Wentworth'], 5440: ['Wentworth'], 2068: ['Willoughby'], 2571: ['Wingecarribee', 'Wollondilly'], 2572: ['Wingecarribee', 'Wollondilly'], 2578: ['Wingecarribee'], 2568: ['Wollondilly'], 2573: ['Wollondilly'], 2500: ['Wollongong'], 2502: ['Wollongong'], 2505: ['Wollongong'], 2506: ['Wollongong'], 2515: ['Wollongong'], 2516: ['Wollongong'], 2517: ['Wollongong'], 2518: ['Wollongong'], 2519: ['Wollongong'], 2525: ['Wollongong'], 2526: ['Wollongong'], 2028: ['Woollahra'], 2263: ['Wyong'], 2611: ['Yass Valley'], 2615: ['Yass Valley'], 2618: ['Yass Valley']}
