import vyshufile
import fresh_tomatoes
robo=vyshufile.cinemas("robo","research on robos",
            "https://tse3.mm.bing.net/th?id=OIP.cc5-9e0-qEn_NWU7eskBPQHaKf&pid=15.1&P=0&w=300&h=300",
                                       "https://www.youtube.com/watch?v=kCyij00blAc")
geethagovindam=vyshufile.cinemas("geetha govindam","love story",
                        "https://tse4.mm.bing.net/th?id=OIP.4ndqPTIEN-2zC8tDhG1RJgHaEJ&pid=15.1&P=0&w=289&h=163",
                                  "https://www.youtube.com/watch?v=U3dqoAHqagk")
taxivalla=vyshufile.cinemas("taxivalla","comic",
                    "https://tse1.mm.bing.net/th?id=OIP.fH_7Fgxk3rVqM6WxTGdSFQHaEZ&pid=15.1&P=0&w=292&h=174",
                            "https://www.youtube.com/watch?v=xOm2Asj08Uk")
happydays=vyshufile.cinemas("happydays","college",
                        "https://tse1.mm.bing.net/th?id=OIP.8ES1RbhL_EFKL7Cuwg1i4gHaHa&pid=15.1&P=0&w=300&h=300",
                            "https://www.youtube.com/watch?v=BYy7gkao5cw")
hello=vyshufile.cinemas("hello","love story",
                        "https://tse2.mm.bing.net/th?id=OIP.bLay41HA-NuwwLBp1KPl4AHaEK&pid=15.1&P=0&w=293&h=166",
                        "https://www.youtube.com/watch?v=5SIWrSCw3eg")
bharathanenennu=vyshufile.cinemas("bharathanenenu","political",
                    "https://tse1.mm.bing.net/th?id=OIP.rcu5DEm4Ss7c3-S2OSxFGAHaJQ&pid=15.1&P=0&w=300&h=300",
                    "https://www.youtube.com/watch?v=t1qP2r4P5kw")
cinemas=[robo,geethagovindam,taxivalla,happydays,hello,bharathanenennu]
fresh_tomatoes.open_movies_page(cinemas)
