/*jslint */
/*global AdobeEdge: false, window: false, document: false, console:false, alert: false */
(function (compId) {

    "use strict";
    var im='../img/images/',
        aud='media/',
        vid='media/',
        js='js/',
        fonts = {
        },
        opts = {
            'gAudioPreloadPreference': 'auto',
            'gVideoPreloadPreference': 'auto'
        },
        resources = [
        ],
        scripts = [
        ],
        symbols = {
            "stage": {
                version: "6.0.0",
                minimumCompatibleVersion: "5.0.0",
                build: "6.0.0.400",
                scaleToFit: "both",
                centerStage: "none",
                resizeInstances: false,
                content: {
                    dom: [
                        {
                            id: 'leftBody',
                            type: 'rect',
                            rect: ['19px', '240px', '110px', '186px', 'auto', 'auto'],
                            clip: 'rect(0px 110px 144px 0px)',
                            borderRadius: ["35px", "35px", "35px", "35px 35px"],
                            fill: ["rgba(240,198,95,1.00)"],
                            stroke: [0,"rgb(0, 0, 0)","none"]
                        },
                        {
                            id: 'leftHead',
                            type: 'ellipse',
                            rect: ['40px', '166px', '67px', '67px', 'auto', 'auto'],
                            borderRadius: ["50%", "50%", "50%", "50%"],
                            fill: ["rgba(240,198,95,1)"],
                            stroke: [0,"rgb(0, 0, 0)","none"]
                        },
                        {
                            id: 'rtBody',
                            type: 'rect',
                            rect: ['417px', '241px', '110px', '186px', 'auto', 'auto'],
                            clip: 'rect(0px 110px 144px 0px)',
                            borderRadius: ["35px", "35px", "35px", "35px 35px"],
                            fill: ["rgba(86,193,78,1.00)"],
                            stroke: [0,"rgb(0, 0, 0)","none"]
                        },
                        {
                            id: 'rtHead',
                            type: 'ellipse',
                            rect: ['438px', '166px', '67px', '67px', 'auto', 'auto'],
                            borderRadius: ["50%", "50%", "50%", "50%"],
                            fill: ["rgba(86,193,78,1.00)"],
                            stroke: [0,"rgb(0, 0, 0)","none"]
                        },
                        {
                            id: 'rightBubble',
                            type: 'group',
                            rect: ['323', '24', '196', '139', 'auto', 'auto'],
                            opacity: '0',
                            c: [
                            {
                                id: 'RoundRect3Copy',
                                type: 'rect',
                                rect: ['0px', '0px', '196px', '93px', 'auto', 'auto'],
                                borderRadius: ["26px", "26px", "26px", "26px 26px"],
                                fill: ["rgba(255,255,255,1.00)"],
                                stroke: [0,"rgb(0, 0, 0)","none"]
                            },
                            {
                                id: 'RectangleCopy',
                                type: 'rect',
                                rect: ['86px', '56px', '31px', '67px', 'auto', 'auto'],
                                fill: ["rgba(255,255,255,1)"],
                                stroke: [0,"rgb(0, 0, 0)","none"],
                                transform: [[],['-38'],['0','-47']]
                            }]
                        },
                        {
                            id: 'heart-02',
                            type: 'image',
                            rect: ['336px', '22px', '85px', '81px', 'auto', 'auto'],
                            opacity: '0',
                            fill: ["rgba(0,0,0,0)",im+"heart-02.svg",'0px','0px'],
                            transform: [[],[],[],['0.83','0.83']]
                        },
                        {
                            id: 'book_red3',
                            symbolName: 'book_red',
                            type: 'rect',
                            rect: ['415px', '28px', 'undefined', 'undefined', 'auto', 'auto'],
                            opacity: '0',
                            filter: [0, 0, 1, 1, 0, 0, 0, 0, "rgba(0,0,0,0)", 0, 0, 0]
                        },
                        {
                            id: 'exclaim',
                            type: 'text',
                            rect: ['487px', '37px', 'auto', 'auto', 'auto', 'auto'],
                            opacity: '0',
                            text: "<p style=\"margin: 0px; text-align: center;\">​<span style=\"font-size: 57px;\">!</span></p>",
                            font: ['Arial, Helvetica, sans-serif', [24, ""], "rgba(0,0,0,1)", "normal", "none", "", "break-word", "nowrap"]
                        },
                        {
                            id: 'leftBubble',
                            type: 'group',
                            rect: ['40', '24', '196', '139', 'auto', 'auto'],
                            opacity: '1',
                            c: [
                            {
                                id: 'RoundRect3',
                                type: 'rect',
                                rect: ['0px', '0px', '196px', '93px', 'auto', 'auto'],
                                borderRadius: ["26px", "26px", "26px", "26px 26px"],
                                fill: ["rgba(255,255,255,1.00)"],
                                stroke: [0,"rgb(0, 0, 0)","none"]
                            },
                            {
                                id: 'Rectangle',
                                type: 'rect',
                                rect: ['60px', '56px', '31px', '67px', 'auto', 'auto'],
                                fill: ["rgba(255,255,255,1)"],
                                stroke: [0,"rgb(0, 0, 0)","none"],
                                transform: [[],['38'],['0','47']]
                            }]
                        },
                        {
                            id: 'glasses',
                            symbolName: 'glasses',
                            type: 'rect',
                            rect: ['49px', '49px', '87', '43', 'auto', 'auto'],
                            opacity: '0'
                        },
                        {
                            id: 'book_red2',
                            symbolName: 'book_red',
                            type: 'rect',
                            rect: ['145px', '33', '47', '73', 'auto', 'auto'],
                            opacity: '0',
                            filter: [0, 0, 1, 1, 0, 0, 0, 0, "rgba(0,0,0,0)", 0, 0, 0]
                        },
                        {
                            id: 'question',
                            type: 'text',
                            rect: ['198px', '40px', 'auto', 'auto', 'auto', 'auto'],
                            opacity: '0',
                            text: "<p style=\"margin: 0px; text-align: center;\">​<span style=\"font-size: 57px;\">?</span></p>",
                            font: ['Arial, Helvetica, sans-serif', [24, ""], "rgba(0,0,0,1)", "normal", "none", "", "break-word", "nowrap"]
                        }
                    ],
                    style: {
                        '${Stage}': {
                            isStage: true,
                            rect: [undefined, undefined, '550px', '400px'],
                            overflow: 'hidden',
                            fill: ["rgba(238,235,235,1.00)"]
                        }
                    }
                },
                timeline: {
                    duration: 11200,
                    autoPlay: true,
                    data: [
                        [
                            "eid10",
                            "opacity",
                            3400,
                            600,
                            "linear",
                            "${rightBubble}",
                            '0.000000',
                            '1'
                        ],
                        [
                            "eid76",
                            "opacity",
                            6000,
                            596,
                            "linear",
                            "${rightBubble}",
                            '1',
                            '0'
                        ],
                        [
                            "eid136",
                            "opacity",
                            8500,
                            500,
                            "linear",
                            "${rightBubble}",
                            '0.000000',
                            '1'
                        ],
                        [
                            "eid171",
                            "opacity",
                            10700,
                            400,
                            "linear",
                            "${rightBubble}",
                            '1',
                            '0'
                        ],
                        [
                            "eid47",
                            "opacity",
                            4000,
                            800,
                            "linear",
                            "${book_red3}",
                            '0.000000',
                            '1'
                        ],
                        [
                            "eid74",
                            "opacity",
                            6000,
                            596,
                            "linear",
                            "${book_red3}",
                            '1',
                            '0'
                        ],
                        [
                            "eid162",
                            "opacity",
                            8900,
                            800,
                            "linear",
                            "${book_red3}",
                            '0.000000',
                            '1'
                        ],
                        [
                            "eid173",
                            "opacity",
                            10700,
                            400,
                            "linear",
                            "${book_red3}",
                            '1',
                            '0'
                        ],
                        [
                            "eid135",
                            "filter.hue-rotate",
                            6596,
                            404,
                            "linear",
                            "${book_red2}",
                            '0deg',
                            '144deg'
                        ],
                        [
                            "eid15",
                            "opacity",
                            1000,
                            600,
                            "linear",
                            "${leftBubble}",
                            '0.000000',
                            '1'
                        ],
                        [
                            "eid68",
                            "opacity",
                            4600,
                            596,
                            "linear",
                            "${leftBubble}",
                            '1',
                            '0'
                        ],
                        [
                            "eid129",
                            "opacity",
                            7000,
                            500,
                            "linear",
                            "${leftBubble}",
                            '0.000000',
                            '1'
                        ],
                        [
                            "eid187",
                            "opacity",
                            10000,
                            400,
                            "linear",
                            "${leftBubble}",
                            '1',
                            '0'
                        ],
                        [
                            "eid22",
                            "opacity",
                            1300,
                            800,
                            "linear",
                            "${glasses}",
                            '0',
                            '1'
                        ],
                        [
                            "eid67",
                            "opacity",
                            4600,
                            596,
                            "linear",
                            "${glasses}",
                            '1',
                            '0'
                        ],
                        [
                            "eid130",
                            "opacity",
                            7200,
                            500,
                            "linear",
                            "${glasses}",
                            '0.000000',
                            '1'
                        ],
                        [
                            "eid185",
                            "opacity",
                            10000,
                            400,
                            "linear",
                            "${glasses}",
                            '1',
                            '0'
                        ],
                        [
                            "eid166",
                            "filter.hue-rotate",
                            8000,
                            400,
                            "linear",
                            "${book_red3}",
                            '0.000000deg',
                            '144deg'
                        ],
                        [
                            "eid78",
                            "top",
                            4500,
                            0,
                            "linear",
                            "${heart-02}",
                            '22px',
                            '22px'
                        ],
                        [
                            "eid138",
                            "top",
                            9200,
                            0,
                            "linear",
                            "${heart-02}",
                            '22px',
                            '22px'
                        ],
                        [
                            "eid52",
                            "opacity",
                            4300,
                            800,
                            "linear",
                            "${exclaim}",
                            '0.000000',
                            '1'
                        ],
                        [
                            "eid73",
                            "opacity",
                            6000,
                            596,
                            "linear",
                            "${exclaim}",
                            '1',
                            '0'
                        ],
                        [
                            "eid163",
                            "opacity",
                            9100,
                            800,
                            "linear",
                            "${exclaim}",
                            '0.000000',
                            '1'
                        ],
                        [
                            "eid175",
                            "opacity",
                            10700,
                            400,
                            "linear",
                            "${exclaim}",
                            '1',
                            '0'
                        ],
                        [
                            "eid84",
                            "height",
                            4500,
                            500,
                            "linear",
                            "${heart-02}",
                            '89px',
                            '102px'
                        ],
                        [
                            "eid90",
                            "height",
                            5100,
                            400,
                            "linear",
                            "${heart-02}",
                            '102px',
                            '81px'
                        ],
                        [
                            "eid96",
                            "height",
                            5600,
                            400,
                            "linear",
                            "${heart-02}",
                            '81px',
                            '102px'
                        ],
                        [
                            "eid102",
                            "height",
                            6100,
                            400,
                            "linear",
                            "${heart-02}",
                            '102px',
                            '81px'
                        ],
                        [
                            "eid139",
                            "height",
                            9200,
                            500,
                            "linear",
                            "${heart-02}",
                            '89px',
                            '102px'
                        ],
                        [
                            "eid140",
                            "height",
                            9800,
                            400,
                            "linear",
                            "${heart-02}",
                            '102px',
                            '81px'
                        ],
                        [
                            "eid141",
                            "height",
                            10300,
                            400,
                            "linear",
                            "${heart-02}",
                            '81px',
                            '102px'
                        ],
                        [
                            "eid142",
                            "height",
                            10800,
                            400,
                            "linear",
                            "${heart-02}",
                            '102px',
                            '81px'
                        ],
                        [
                            "eid77",
                            "left",
                            4500,
                            0,
                            "linear",
                            "${heart-02}",
                            '336px',
                            '336px'
                        ],
                        [
                            "eid145",
                            "left",
                            9200,
                            0,
                            "linear",
                            "${heart-02}",
                            '336px',
                            '336px'
                        ],
                        [
                            "eid43",
                            "opacity",
                            3700,
                            800,
                            "linear",
                            "${heart-02}",
                            '0.000000',
                            '1'
                        ],
                        [
                            "eid75",
                            "opacity",
                            6000,
                            596,
                            "linear",
                            "${heart-02}",
                            '1',
                            '0'
                        ],
                        [
                            "eid143",
                            "opacity",
                            8700,
                            500,
                            "linear",
                            "${heart-02}",
                            '0.000000',
                            '1'
                        ],
                        [
                            "eid144",
                            "opacity",
                            10700,
                            400,
                            "linear",
                            "${heart-02}",
                            '1',
                            '0'
                        ],
                        [
                            "eid30",
                            "opacity",
                            1700,
                            800,
                            "linear",
                            "${book_red2}",
                            '0.000000',
                            '1'
                        ],
                        [
                            "eid66",
                            "opacity",
                            4600,
                            596,
                            "linear",
                            "${book_red2}",
                            '1',
                            '0'
                        ],
                        [
                            "eid131",
                            "opacity",
                            7400,
                            500,
                            "linear",
                            "${book_red2}",
                            '0.000000',
                            '1'
                        ],
                        [
                            "eid183",
                            "opacity",
                            10000,
                            400,
                            "linear",
                            "${book_red2}",
                            '1',
                            '0'
                        ],
                        [
                            "eid83",
                            "width",
                            4500,
                            500,
                            "linear",
                            "${heart-02}",
                            '85px',
                            '101px'
                        ],
                        [
                            "eid89",
                            "width",
                            5100,
                            400,
                            "linear",
                            "${heart-02}",
                            '101px',
                            '79px'
                        ],
                        [
                            "eid95",
                            "width",
                            5600,
                            400,
                            "linear",
                            "${heart-02}",
                            '79px',
                            '101px'
                        ],
                        [
                            "eid101",
                            "width",
                            6100,
                            400,
                            "linear",
                            "${heart-02}",
                            '101px',
                            '79px'
                        ],
                        [
                            "eid146",
                            "width",
                            9200,
                            500,
                            "linear",
                            "${heart-02}",
                            '85px',
                            '101px'
                        ],
                        [
                            "eid147",
                            "width",
                            9800,
                            400,
                            "linear",
                            "${heart-02}",
                            '101px',
                            '79px'
                        ],
                        [
                            "eid148",
                            "width",
                            10300,
                            400,
                            "linear",
                            "${heart-02}",
                            '79px',
                            '101px'
                        ],
                        [
                            "eid149",
                            "width",
                            10800,
                            400,
                            "linear",
                            "${heart-02}",
                            '101px',
                            '79px'
                        ],
                        [
                            "eid35",
                            "opacity",
                            2100,
                            800,
                            "linear",
                            "${question}",
                            '0.000000',
                            '1'
                        ],
                        [
                            "eid65",
                            "opacity",
                            4600,
                            596,
                            "linear",
                            "${question}",
                            '1',
                            '0'
                        ],
                        [
                            "eid132",
                            "opacity",
                            7600,
                            500,
                            "linear",
                            "${question}",
                            '0.000000',
                            '1'
                        ],
                        [
                            "eid181",
                            "opacity",
                            10000,
                            400,
                            "linear",
                            "${question}",
                            '1',
                            '0'
                        ]
                    ]
                }
            },
            "guy": {
                version: "6.0.0",
                minimumCompatibleVersion: "5.0.0",
                build: "6.0.0.400",
                scaleToFit: "none",
                centerStage: "none",
                resizeInstances: false,
                content: {
                    dom: [
                        {
                            rect: ['0px', '74px', '99px', '189px', 'auto', 'auto'],
                            borderRadius: ['34px', '34px', '34px', '34px 34px'],
                            type: 'rect',
                            id: 'RoundRect',
                            stroke: [0, 'rgba(0,0,0,1)', 'none'],
                            clip: 'rect(0px 99px 129px 0px)',
                            fill: ['rgba(192,192,192,1)']
                        },
                        {
                            rect: ['16px', '0px', '67px', '67px', 'auto', 'auto'],
                            borderRadius: ['50%', '50%', '50%', '50%'],
                            id: 'Ellipse',
                            stroke: [0, 'rgb(0, 0, 0)', 'none'],
                            type: 'ellipse',
                            fill: ['rgba(192,192,192,1)']
                        }
                    ],
                    style: {
                        '${symbolSelector}': {
                            isStage: 'true',
                            rect: [undefined, undefined, '99px', '263px']
                        }
                    }
                },
                timeline: {
                    duration: 0,
                    autoPlay: true,
                    data: [

                    ]
                }
            },
            "glasses": {
                version: "6.0.0",
                minimumCompatibleVersion: "5.0.0",
                build: "6.0.0.400",
                scaleToFit: "none",
                centerStage: "none",
                resizeInstances: false,
                content: {
                    dom: [
                        {
                            rect: ['-43px', '-21px', '174px', '85px', 'auto', 'auto'],
                            id: 'icon_items-04',
                            transform: [[], [], [], ['0.5', '0.5']],
                            type: 'image',
                            fill: ['rgba(0,0,0,0)', 'images/icon_items-04.svg', '0px', '0px']
                        }
                    ],
                    style: {
                        '${symbolSelector}': {
                            isStage: 'true',
                            rect: [undefined, undefined, '87px', '43px']
                        }
                    }
                },
                timeline: {
                    duration: 0,
                    autoPlay: true,
                    data: [

                    ]
                }
            },
            "book_red": {
                version: "6.0.0",
                minimumCompatibleVersion: "5.0.0",
                build: "6.0.0.400",
                scaleToFit: "none",
                centerStage: "none",
                resizeInstances: false,
                content: {
                    dom: [
                        {
                            rect: ['-16px', '-25px', '79px', '123px', 'auto', 'auto'],
                            id: 'icon_items-032',
                            transform: [[], [], [], ['0.59', '0.59']],
                            type: 'image',
                            fill: ['rgba(0,0,0,0)', 'images/icon_items-03.svg', '0px', '0px']
                        }
                    ],
                    style: {
                        '${symbolSelector}': {
                            isStage: 'true',
                            rect: [undefined, undefined, '47px', '73px']
                        }
                    }
                },
                timeline: {
                    duration: 0,
                    autoPlay: true,
                    data: [

                    ]
                }
            }
        };

    AdobeEdge.registerCompositionDefn(compId, symbols, fonts, scripts, resources, opts);

    if (!window.edge_authoring_mode) AdobeEdge.getComposition(compId).load("bubble_talking_edgeActions.js");
})("EDGE-7901779");
