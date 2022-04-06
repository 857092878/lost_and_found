$(window).load(function() {
    $(".loading").fadeOut()
})
$(function() {
    echarts_1();
    // echarts_2();
    echarts_3();
    echarts_4();
    zb1();
    zb2();
    zb3();
    zb4();
    zb5();
    zb6();

    function echarts_1() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart1'));
        var option = {
            tooltip: {
                trigger: 'item',
                formatter: "{b} : {c} ({d}%)"
            },
            legend: {
                right: 0,
                top: 30,
                height: 160,
                itemWidth: 10,
                itemHeight: 10,
                itemGap: 10,
                textStyle: {
                    color: 'rgba(255,255,255,.6)',
                    fontSize: 12
                },
                orient: 'vertical',
                data: ['TES', 'JDG', 'V5', 'IG', 'SN']
            },
            calculable: true,
            series: [{
                name: ' ',
                color: ['#62c98d', '#2f89cf', '#4cb9cf', '#53b666', '#62c98d', '#205acf', '#c9c862', '#c98b62', '#c962b9', '#7562c9', '#c96262', '#c25775', '#00b7be'],
                type: 'pie',
                radius: [30, 70],
                center: ['35%', '50%'],
                roseType: 'radius',
                label: {
                    normal: {
                        show: true
                    },
                    emphasis: {
                        show: true
                    }
                },

                lableLine: {
                    normal: {
                        show: true
                    },
                    emphasis: {
                        show: true
                    }
                },

                data: [{
                        value: 10,
                        name: 'IG'
                    },
                    {
                        value: 5,
                        name: 'SN'
                    },
                    {
                        value: 15,
                        name: 'V5'
                    },
                    {
                        value: 25,
                        name: 'TES'
                    },
                    {
                        value: 20,
                        name: 'JDG'
                    },

                ]
            }, ]
        };
        $.ajax({
            url:"/chart/index/sort/",
            type: "get",
            dataType: "JSON",
                success: function (res) {
                    option.legend.data = res.context.legend
                    option.series[0].data = res.context.data
                    myChart.setOption(option);

                }
        })
        myChart.setOption(option);
    }
    function echarts_3() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart3'));
        var option = {
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    lineStyle: {
                        color: '#57617B'
                    }
                }
            },
            legend: {

                //icon: 'vertical',
                data: ['挂失', '捡到'],
                //align: 'center',
                // right: '35%',
                top: '0',
                textStyle: {
                    color: "#fff"
                },
                // itemWidth: 15,
                // itemHeight: 15,
                itemGap: 20,
            },
            grid: {
                left: '0',
                right: '30',
                top: '10',
                bottom: '20',
                containLabel: true
            },
            xAxis: {
                type: 'category',
                boundaryGap: false,
                axisLabel: {
                    show: true,
                    textStyle: {
                        color: 'rgba(255,255,255,1)',
                        fontSize: 11
                    }
                },
                axisLine: {
                    lineStyle: {
                        color: 'rgba(255,255,255,.1)'
                    }
                },
                data: ['\nWE\nJiumeng', '\nLGD\nxiye', '\nTES\nknight', '\nJDG\nKanavi', '\nTES\nJackeyLove', '\nSN\nSofM', '\nV5\nMole', '\nEDG\nScout',
                    '\nSN\nhuanfeng', '\nFPX\nDoinb', '\nIG\nNing', '\nV5\nSamd'
                ]
            },
            yAxis: [{
                axisLabel: {
                    show: true,
                    textStyle: {
                        color: 'rgba(255,255,255,.6)'
                    }
                },
                axisLine: {
                    lineStyle: {
                        color: 'rgba(255,255,255,.1)'
                    }
                },
                splitLine: {
                    lineStyle: {
                        color: 'rgba(255,255,255,.1)'
                    }
                }
            }],
            series: [{
                name: '挂失',
                type: 'line',
                smooth: true,
                symbol: 'circle',
                symbolSize: 5,
                showSymbol: false,
                lineStyle: {
                    normal: {
                        width: 2
                    }
                },
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(24, 163, 64, 0.3)'
                        }, {
                            offset: 0.8,
                            color: 'rgba(24, 163, 64, 0)'
                        }], false),
                        shadowColor: 'rgba(0, 0, 0, 0.1)',
                        shadowBlur: 10
                    }
                },
                itemStyle: {
                    normal: {
                        color: '#cdba00',
                        borderColor: 'rgba(137,189,2,0.27)',
                        borderWidth: 12
                    }
                },
                data: [205, 191, 239, 169, 205, 125, 162, 136, 189, 157, 121, 158]
            }, {
                name: '捡到',
                type: 'line',
                smooth: true,
                symbol: 'circle',
                symbolSize: 5,
                showSymbol: false,
                lineStyle: {
                    normal: {
                        width: 2
                    }
                },
                areaStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(39, 122,206, 0.3)'
                        }, {
                            offset: 0.8,
                            color: 'rgba(39, 122,206, 0)'
                        }], false),
                        shadowColor: 'rgba(0, 0, 0, 0.1)',
                        shadowBlur: 10
                    }
                },
                itemStyle: {
                    normal: {
                        color: '#277ace',
                        borderColor: 'rgba(0,136,212,0.2)',
                        borderWidth: 12
                    }
                },
                data: [266, 289, 299, 345, 278, 375, 270, 270, 286, 315, 304, 220]
            }]
        };
        $.ajax({
        url:"/chart/index/time/",
        type: "get",
        dataType: "JSON",
            success: function (res) {
                option.xAxis.data = res.day_list
                option.series[0].data = res.lost_count_list
                option.series[1].data = res.found_count_list
                myChart.setOption(option);

            }
        })
        myChart.setOption(option);
    }

    function echarts_4() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart4'));
        var option = {
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    lineStyle: {
                        color: '#57617B'
                    }
                }
            },
            legend: {

                data: [{
                        "name": "掉的位置"
                    },
                ],
                top: "0%",
                textStyle: {
                    color: "rgba(255,255,255,1)", //图例文字
                    fontSize: "16"
                }
            },

            xAxis: [{
                type: "category",

                data: ['BLG'],
                axisLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)"
                    }
                },
                axisLabel: {
                    textStyle: {
                        color: "rgb(255,255,255)",
                        fontSize: '16',
                    },
                },

            }, ],
            "yAxis": [{
                    "type": "value",
                    "name": "次数",
                    "min": 0,
                    "interval": 10,
                    "axisLabel": {
                        "show": true,

                    },
                    axisLine: {
                        lineStyle: {
                            color: 'rgba(255,255,255,1)'
                        }
                    }, //左线色
                    splitLine: {
                        show: true,
                        lineStyle: {
                            color: "rgba(255,255,255,0.5)"
                        }
                    }, //x轴线
                },
            ],
            "grid": {
                "top": "10%",
                "right": "30",
                "bottom": "30",
                "left": "30",
            },
            "series": [{
                    "name": "掉的位置",

                    "type": "bar",
                    "data": [17],
                    "barWidth": "auto",
                    "itemStyle": {
                        "normal": {
                            "color": {
                                "type": "linear",
                                "x": 0,
                                "y": 0,
                                "x2": 0,
                                "y2": 1,
                                "colorStops": [{
                                        "offset": 0,
                                        "color": "#67E0E3"
                                    },

                                    {
                                        "offset": 1,
                                        "color": "#67E0E3"
                                    }
                                ],
                                "globalCoord": false
                            }
                        }
                    }
                },

            ]
        };

         $.ajax({
            url:"/chart/index/location/",
            type: "get",
            dataType: "JSON",
                success: function (res) {
                    option.xAxis[0].data = res.location_key
                    option.series[0].data = res.location_value
                    myChart.setOption(option);

                }
        })

    }


    function zb1() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb1'));
        var v1 = 0
        option = {
            tooltip: {
                trigger: 'item',
            },
            series: [{

                type: 'pie',
                radius: ['60%', '70%'],
                color: '#37A2DA',
                label: {
                    normal: {
                        position: 'center'
                    }
                },
                data: [{
                    value: v1,
                    label: {
                        normal: {
                            formatter: v1 + '',
                            textStyle: {
                                fontSize: 20,
                                color: '#fff',
                            }
                        }
                    }
                }, {
                    label: {
                        normal: {
                            formatter: function(params) {
                                return '今日挂失'
                            },
                            textStyle: {
                                color: '#aaa',
                                fontSize: 12
                            }
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: 'rgba(255,255,255,.2)'
                        },
                        emphasis: {
                            color: '#fff'
                        }
                    },
                }]
            }]
        };
        $.ajax({
            url:"/chart/index/resouse/",
             dataType: "JSON",
             data: option.series[0].data[0].value,
                success: function (res) {
                    option.series[0].data[0].value = res.today_lost_all
                    option.series[0].data[0].label.normal.formatter = res.today_lost_all + ""
                    // option.series[0].data[0].value = 0
                    myChart.setOption(option);
                    window.addEventListener("resize", function() {
                        myChart.resize();
                    });
                }
        })

    }

    function zb2() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb2'));
        var v1 = 0 //胜利
        option = {
            tooltip: {
                trigger: 'item',
            },
            series: [{

                type: 'pie',
                radius: ['60%', '70%'],
                color: '#32C5E9',
                label: {
                    normal: {
                        position: 'center'
                    }
                },
                data: [{
                    value: v1,
                    label: {
                        normal: {
                            formatter: v1 + '',
                            textStyle: {
                                fontSize: 20,
                                color: '#fff',
                            }
                        }
                    }
                }, {
                    label: {
                        normal: {
                            formatter: function(params) {
                                return '累计挂失'
                            },
                            textStyle: {
                                color: '#aaa',
                                fontSize: 12
                            }
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: 'rgba(255,255,255,.2)'
                        },
                        emphasis: {
                            color: '#fff'
                        }
                    },
                }]
            }]
        };
        $.ajax({
            url:"/chart/index/resouse/",
             dataType: "JSON",
                success: function (res) {
                    option.series[0].data[0].value = res.all_lost_all
                    option.series[0].data[0].label.normal.formatter = res.all_lost_all + ""
                    myChart.setOption(option);
                    window.addEventListener("resize", function() {
                        myChart.resize();
                    });
                }
        })

    }

    function zb3() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb3'));
       var v1 = 0 //胜利
        option = {
            tooltip: {
                trigger: 'item',
            },
            series: [{

                type: 'pie',
                radius: ['60%', '70%'],
                color: '#67E0E3',
                label: {
                    normal: {
                        position: 'center'
                    }
                },
                data: [{
                    value: v1,
                    label: {
                        normal: {
                            formatter: v1 + '',
                            textStyle: {
                                fontSize: 20,
                                color: '#fff',
                            }
                        }
                    }
                }, {
                    label: {
                        normal: {
                            formatter: function(params) {
                                return '今日捡到'
                            },
                            textStyle: {
                                color: '#aaa',
                                fontSize: 12
                            }
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: 'rgba(255,255,255,.2)'
                        },
                        emphasis: {
                            color: '#fff'
                        }
                    },
                }]
            }]
        };
        $.ajax({
            url:"/chart/index/resouse/",
             dataType: "JSON",
                success: function (res) {
                    option.series[0].data[0].value = res.today_found_all
                    option.series[0].data[0].label.normal.formatter = res.today_found_all + ""
                    myChart.setOption(option);
                    window.addEventListener("resize", function() {
                        myChart.resize();
                    });
                }
        })

    }

    function zb4() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb4'));
       var v1 = 151 //胜利
        option = {
            tooltip: {
                trigger: 'item',
            },
            series: [{

                type: 'pie',
                radius: ['60%', '70%'],
                color: '#9FE6B8',
                label: {
                    normal: {
                        position: 'center'
                    }
                },
                data: [{
                    value: v1,
                    label: {
                        normal: {
                            formatter: v1 + '',
                            textStyle: {
                                fontSize: 20,
                                color: '#fff',
                            }
                        }
                    }
                }, {
                    label: {
                        normal: {
                            formatter: function(params) {
                                return '未还的'
                            },
                            textStyle: {
                                color: '#aaa',
                                fontSize: 12
                            }
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: 'rgba(255,255,255,.2)'
                        },
                        emphasis: {
                            color: '#fff'
                        }
                    },
                }]
            }]
        };
        $.ajax({
            url:"/chart/index/resouse/",
             dataType: "JSON",
                success: function (res) {
                    option.series[0].data[0].value = res.all_found_count
                    option.series[0].data[0].label.normal.formatter = res.all_found_count + ""
                    myChart.setOption(option);
                    window.addEventListener("resize", function() {
                        myChart.resize();
                    });
                }
        })

    }

    function zb5() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb5'));
        var v1 = 5 //胜利
        option = {
            tooltip: {
                trigger: 'item',
            },
            series: [{

                type: 'pie',
                radius: ['60%', '70%'],
                color: '#FFDB5C',
                label: {
                    normal: {
                        position: 'center'
                    }
                },
                data: [{
                    value: v1,
                    label: {
                        normal: {
                            formatter: v1 + '',
                            textStyle: {
                                fontSize: 20,
                                color: '#fff',
                            }
                        }
                    }
                }, {
                    label: {
                        normal: {
                            formatter: function(params) {
                                return '未找到'
                            },
                            textStyle: {
                                color: '#aaa',
                                fontSize: 12
                            }
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: 'rgba(255,255,255,.2)'
                        },
                        emphasis: {
                            color: '#fff'
                        }
                    },
                }]
            }]
        };
        $.ajax({
            url:"/chart/index/resouse/",
             dataType: "JSON",
                success: function (res) {
                    option.series[0].data[0].value = res.all_lost_count
                    option.series[0].data[0].label.normal.formatter = res.all_lost_count + ""
                    myChart.setOption(option);
                    window.addEventListener("resize", function() {
                        myChart.resize();
                    });
                }
        })

    }

    function zb6() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb6'));
        var v1 = 45 //胜利
        option = {
            tooltip: {
                trigger: 'item',
            },
            series: [{

                type: 'pie',
                radius: ['60%', '70%'],
                color: '#FB7293',
                label: {
                    normal: {
                        position: 'center'
                    }
                },
                data: [{
                    value: v1,
                    label: {
                        normal: {
                            formatter: v1 + '',
                            textStyle: {
                                fontSize: 20,
                                color: '#fff',
                            }
                        }
                    }
                }, {
                    label: {
                        normal: {
                            formatter: function(params) {
                                return '累计捡到'
                            },
                            textStyle: {
                                color: '#aaa',
                                fontSize: 12
                            }
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: 'rgba(255,255,255,.2)'
                        },
                        emphasis: {
                            color: '#fff'
                        }
                    },
                }]
            }]
        };
        $.ajax({
            url:"/chart/index/resouse/",
             dataType: "JSON",
                success: function (res) {
                    option.series[0].data[0].value = res.all_found_all
                    option.series[0].data[0].label.normal.formatter = res.all_found_all + ""
                    myChart.setOption(option);
                    window.addEventListener("resize", function() {
                        myChart.resize();
                    });
                }
        })

    }
})