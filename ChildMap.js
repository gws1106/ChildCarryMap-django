import axios from "axios";
import { useEffect, useState } from "react";
import { CustomOverlayMap, Map, MapMarker } from "react-kakao-maps-sdk";

import {
  TbBabyBottle,
  TbPill,
} from "react-icons/tb";

import {
  MdLocalConvenienceStore,
} from "react-icons/md";

import {
  FaBars,
  FaStore,
  FaRegHospital,
  FaParking,
  FaRestroom,
  FaFireExtinguisher,
  FaDollarSign,
} from "react-icons/fa"

import {
  PiPoliceCarBold,
} from "react-icons/pi"

import waterpark from "../image/waterpark.png";
import fountain from "../image/fountain.png";
import swim from "../image/swim.png";

import React, { PureComponent } from 'react';
import { Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, ResponsiveContainer } from 'recharts';


function ChildMap() {

  //아이콘 클릭시 보이기 사라지기
  //수유실
  const [isNurseClick, setIsNurseClick] = useState(false);
  const nurseClicked = () => setIsNurseClick(!isNurseClick);

  //화장실
  const [isToiletClick, setIsToiletClick] = useState(false);
  const toiletClicked = () => setIsToiletClick(!isToiletClick);

  //편의점
  const [isConvClick, setIsConvClick] = useState(false);
  const convClicked = () => setIsConvClick(!isConvClick);

  //드러그스토어(다이소,올리브영 등)
  const [isStoreClick, setIsStoreClick] = useState(false);
  const storeClicked = () => setIsStoreClick(!isStoreClick);

  //약국
  const [isPillClick, setIsPillClick] = useState(false);
  const pillClicked = () => setIsPillClick(!isPillClick);

  //병원
  const [isHospitalClick, setIsHospitalClick] = useState(false);
  const hospitalClicked = () => setIsHospitalClick(!isHospitalClick);

  //경찰서
  const [isPoliceClick, setIsPoliceClick] = useState(false);
  const policeClicked = () => setIsPoliceClick(!isPoliceClick);

  //소방서
  const [isFireClick, setIsFireClick] = useState(false);
  const fireClicked = () => setIsFireClick(!isFireClick);

  //민영주차장
  // const [isParkClick, setIsParkClick] = useState(false);
  // const parkClicked = () => setIsParkClick(!isParkClick);

  //공영주차장
  const [isFreeClick, setIsFreeClick] = useState(false);
  const freeClicked = () => setIsFreeClick(!isFreeClick);

  //토글버튼 눌렸는지 확인
  const toggle = () => setIsOpen(!isOpen);

  //사이드바 열렸는지 확인
  const [isOpen, setIsOpen] = useState(false);

  //사이드바 메뉴 목록
  const menuItem = [
    {
      name: "수유실",
      icon: <TbBabyBottle color="#3170B9"/>,
      clicked: nurseClicked,
    },
    {
      name: "화장실",
      icon: <FaRestroom color="#3170B9"/>,
      clicked: toiletClicked,
    },
    {
      name: "편의점",
      icon: <MdLocalConvenienceStore color="#3170B9"/>,
      clicked: convClicked,
    },
    {
      name: "드러그스토어",
      icon: <FaStore color="#3170B9"/>,
      clicked: storeClicked,
    },
    {
      name: "약국",
      icon: <TbPill color="#3170B9"/>,
      clicked: pillClicked,
    },
    {
      name: "병원",
      icon: <FaRegHospital color="#3170B9"/>,
      clicked: hospitalClicked,
    },
    {
      name: "경찰서",
      icon: <PiPoliceCarBold color="#3170B9"/>,
      clicked: policeClicked,
    },
    {
      name: "소방서",
      icon: <FaFireExtinguisher color="#3170B9"/>,
      clicked: fireClicked,
    },
    {
      name: "공영주차장",
      icon: <FaParking color="#3170B9"/>,
      clicked: freeClicked,
    },
  ]

  // Geolocation 예제
  const [location, setLocation] = useState({
    center: {
      lat: 33.450701,
      lng: 126.570667,
    },
    errMsg: null,
    isLoading: true,
  })

  useEffect(() => {
    if (navigator.geolocation) {
      // GeoLocation을 이용해서 접속 위치를 얻어옵니다
      navigator.geolocation.getCurrentPosition(
        (position) => {
          setLocation((prev) => ({
            ...prev,
            center: {
              lat: position.coords.latitude, // 위도
              lng: position.coords.longitude, // 경도
            },
            isLoading: false,
          }))
        },
        (err) => {
          setLocation((prev) => ({
            ...prev,
            errMsg: err.message,
            isLoading: false,
          }))
        }
      )
    } else {
      // HTML5의 GeoLocation을 사용할 수 없을때 마커 표시 위치와 인포윈도우 내용을 설정합니다
      setLocation((prev) => ({
        ...prev,
        errMsg: "geolocation을 사용할수 없어요..",
        isLoading: false,
      }))
    }
  }, [])


  //장소 데이터 받아오기
  //물놀이시설 데이터 받아오기
  const [wptype1, setWptype1] = useState([]);
  useEffect(() => {
    axios
      .get('http://BackEndServer-ALB-1230290334.us-east-2.elb.amazonaws.com/map/wptypeids/1')
      .then(json => {
        // console.log(json.data[0].waterplayvalue01);
        setWptype1(json.data); 
      })
  }, []);

  //수영장 데이터 받아오기
  const [wptype2, setWptype2] = useState([]);
  useEffect(() => {
    axios
      .get('http://BackEndServer-ALB-1230290334.us-east-2.elb.amazonaws.com/map/wptypeids/2')
      .then(json => {
        // console.log(json.data);
        // console.log(json.data[0].waterplayscorefacidesc);
        setWptype2(json.data);
      })
  }, []);

  //바닥분수 데이터 받아오기
  const [wptype3, setWptype3] = useState([]);
  useEffect(() => {
    axios
      .get('http://BackEndServer-ALB-1230290334.us-east-2.elb.amazonaws.com/map/wptypeids/3')
      .then(json => {
        // console.log(json.data);
        setWptype3(json.data);
      })
  }, []);


  //수유실 데이터 받아오기
  const [nurse, setNurse] = useState([]);
  useEffect(() => {
    axios
      .get('http://BackEndServer-ALB-1230290334.us-east-2.elb.amazonaws.com/map/toilettypes/%EC%88%98%EC%9C%A0%EC%8B%A4/')
      .then(json => {
        // console.log(json.data);
        setNurse(json.data);
      })
  }, []);

  //화장실 데이터 받아오기
  const [toilet, setToilet] = useState([]);
  useEffect(() => {
    axios
      .get('http://BackEndServer-ALB-1230290334.us-east-2.elb.amazonaws.com/map/toilettypes/%ED%99%94%EC%9E%A5%EC%8B%A4/')
      .then(json => {
        // console.log(json.data);
        setToilet(json.data);
      })
  }, []);

  //편의점 데이터 받아오기
  const [conv, setConv] = useState([]);
  useEffect(() => {
    axios
      .get('http://BackEndServer-ALB-1230290334.us-east-2.elb.amazonaws.com/map/convtypes/%ED%8E%B8%EC%9D%98%EC%A0%90/')
      .then(json => {
        // console.log(json.data);
        setConv(json.data);
      })
  }, []);

  //드러그 스토어 데이터 받아오기
  const [store, setStore] = useState([]);
  useEffect(() => {
    axios
      .get('http://BackEndServer-ALB-1230290334.us-east-2.elb.amazonaws.com/map/convtypes/%EB%93%9C%EB%9F%AC%EA%B7%B8%EC%8A%A4%ED%86%A0%EC%96%B4/')
      .then(json => {
        // console.log(json.data);
        setStore(json.data);
      })
  }, []);

  //약국 데이터 받아오기
  const [pill, setPill] = useState([]);
  useEffect(() => {
    axios
      .get('http://BackEndServer-ALB-1230290334.us-east-2.elb.amazonaws.com/map/meditypes/%EC%95%BD%EA%B5%AD/')
      .then(json => {
        // console.log(json.data);
        setPill(json.data);
      })
  }, []);

  //병원 데이터 받아오기
  const [hospital, setHospital] = useState([]);
  useEffect(() => {
    axios
      .get('http://BackEndServer-ALB-1230290334.us-east-2.elb.amazonaws.com/map/meditypes/%EB%B3%91%EC%9B%90/')
      .then(json => {
        // console.log(json.data);
        setHospital(json.data);
      })
  }, []);

  //경찰서 데이터 받아오기
  const [police, setPolice] = useState([]);
  useEffect(() => {
    axios
      .get('http://BackEndServer-ALB-1230290334.us-east-2.elb.amazonaws.com/map/safe112alls/')
      .then(json => {
        // console.log(json.data);
        setPolice(json.data);
      })
  }, []);

  //소방서 데이터 받아오기
  const [fire, setFire] = useState([]);
  useEffect(() => {
    axios
      .get('http://BackEndServer-ALB-1230290334.us-east-2.elb.amazonaws.com/map/safe119alls/')
      .then(json => {
        // console.log(json.data);
        setFire(json.data);
      })
  }, []);

  //민영 주차장 데이터 받아오기
  const [park, setPark] = useState([]);
  useEffect(() => {
    axios
      .get('http://BackEndServer-ALB-1230290334.us-east-2.elb.amazonaws.com/map/parkingtypes/%EB%AF%BC%EC%98%81/')
      .then(json => {
        // console.log(json.data);
        setPark(json.data);
      })
  }, []);

  //공영 주차장 데이터 받아오기
  const [free, setFree] = useState([]);
  useEffect(() => {
    axios
      .get('http://BackEndServer-ALB-1230290334.us-east-2.elb.amazonaws.com/map/parkingtypes/%EA%B3%B5%EC%98%81/')
      .then(json => {
        // console.log(json.data);
        setFree(json.data);
      })
  }, []);

  //물놀이 카테고리 만들기
  const markerImageSrc =
    "../image/mulnori-sprite.png"
  // const imageSize = { width: 22, height: 26 }
  // const spriteSize = { width: 30, height: 90 }

  const [selectedCategory, setSelectedCategory] = useState("waterpark")

  useEffect(() => {
    const waterground = document.getElementById("waterpark")
    const fountain = document.getElementById("fountain")
    const pool = document.getElementById("pool")

    if (selectedCategory === "waterpark") {
      // 커피숍 카테고리를 선택된 스타일로 변경하고
      waterground.className = "menu_selected"

      // 편의점과 주차장 카테고리는 선택되지 않은 스타일로 바꿉니다
      fountain.className = ""
      pool.className = ""
    } else if (selectedCategory === "fountain") {
      // 편의점 카테고리가 클릭됐을 때

      // 편의점 카테고리를 선택된 스타일로 변경하고
      waterground.className = ""
      fountain.className = "menu_selected"
      pool.className = ""
    } else if (selectedCategory === "pool") {
      // 주차장 카테고리가 클릭됐을 때

      // 주차장 카테고리를 선택된 스타일로 변경하고
      waterground.className = ""
      fountain.className = ""
      pool.className = "menu_selected"
    }
  }, [selectedCategory])


  //커스텀 오버레이
  const CustomOverlay = ({ position, title, image, address, newAddress }) => {
    const [isCLick, setIsClick] = useState(false);
    return (
      <>
        <MapMarker
          position={position}
          onClick={() => setIsClick(true)}
          image={{
            src: image, // 마커이미지의 주소입니다
            size: {
              width: 30,
              height: 30
            }, // 마커이미지의 크기입니다
          }}
        />

        {/* 마커 클릭시 간단한 정보 알려주는 부분 */}
        {isCLick && (
          <CustomOverlayMap position={position}>
            <div className='t_wrap'>
              <div className='t_info'>
                <div className='t_title'>
                  {title}
                  <div
                    className='t_close'
                    onClick={() => setIsClick(false)}
                    title='닫기'
                  ></div>
                </div>
                <div className='t_body'>
                  <div className='t_img'>
                    <img
                      src={image}
                      width="73"
                      height="70"
                      alt={title}
                    />
                  </div>
                  <div className="t_desc">
                    <div className="t_jibun ellipsis">
                      구주소: {address}
                    </div>
                    <div>
                      <div>
                        {/* {phone} */}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </CustomOverlayMap>
        )}
      </>
    )
  }


  const WaterCustomOverlay = ({
    position,
    markerImage,
    image,
    title,
    value01,
    value02,
    value03,
    oAddress,
    phone,
    scoreToilet,
    scoreConv,
    scoreDrug,
    scoreMedi,
    score112,
    score119,
    scorePark,
    scoreTotal,
    name01,
    scoreColor,
    scoreReview
  }) => {
    //마커 클릭시
    const [isWaterparkClick, setIsWaterparkClick] = useState(false);

    //상세페이지 클릭시
    const [isDetailClick, setIsDetailClick] = useState(false);

    //그래프데이터
    const data = [
      {
        subject: '화장실',
        score: scoreToilet * 100,
        fullMark: 50,
      },

      {
        subject: '편의점',
        score: scoreConv * 100,
        fullMark: 50,
      },

      {
        subject: '드럭스토어',
        score: scoreDrug * 100,
        fullMark: 50,
      },

      {
        subject: '의약시설',
        score: scoreMedi * 100,
        fullMark: 50,
      },

      {
        subject: '112',
        score: score112 * 100,
        fullMark: 50,
      },

      {
        subject: '119',
        score: score119 * 100,
        fullMark: 50,
      },

      {
        subject: '주차장',
        score: scorePark * 100,
        fullMark: 50,
      }
    ]
    return (
      <>
        <MapMarker
          position={position}
          // onClick={() => setIsClick(true)}
          image={markerImage}
          onClick={() => setIsWaterparkClick(true)}
        />

        {isWaterparkClick &&
          (
            <CustomOverlayMap position={position}>
              <div className='wrap'>
                <div className='info'>
                  <div className='title'>
                    {title}
                    <div
                      className='close'
                      onClick={() => setIsWaterparkClick(false)}
                      title='닫기'
                    ></div>
                  </div>
                  <div className='body'>
                    <div className='img'>
                      <img
                        src={image}
                        width="73"
                        height="110"
                        alt={title}
                      />
                    </div>
                    <div className="desc">
                      <div className="jibun ellipsis">
                        <div
                          style={{
                            marginBottom: "15px",
                          }}>
                          주소 : {oAddress}
                          <br />
                          운영시간 : {value01} <br /> <div style={{ color: 'tomato', }}>{value02}</div>
                          전화번호 : {phone}
                        </div>

                        <div>
                          <button onClick={() => setIsDetailClick(true)} style={{ color: "blue", }}>상세페이지</button>
                          <button onClick={() => setIsDetailClick(true)} style={{ color: "blue", }}>길찾기</button>
                        </div>
                      </div>

                      {/* 상세데이터 */}
                      {
                        isDetailClick && (
                          <CustomOverlayMap position={position}>
                            <div style={{
                              width: "1050px",
                              height: "500px",
                              backgroundColor: "white",
                              border: "2px solid black",
                              borderRadius: "10px",
                              // overflow: "auto",
                              padding: "10px",
                              // justifyContent: "center",
                            }}>
                              <img
                                alt="close"
                                width="20"
                                height="20"
                                src="https://t1.daumcdn.net/localimg/localimages/07/mapjsapi/2x/bt_close.gif"
                                style={{
                                  position: "absolute",
                                  right: "5px",
                                  top: "5px",
                                  cursor: "pointer",
                                }}
                                onClick={() => setIsDetailClick(false)}
                              />

                              <div style={{
                                padding: "10px",
                                // overflow: "auto",
                                justifyContent: "center",
                                alignContent: "center",
                              }}>
                                {/* 1번구역 */}
                                <div
                                  style={{
                                    border: "2px solid tomato",
                                    width: "300px",
                                    height: "450px",
                                    float: "left",
                                    margin: "10px",
                                    padding: "10px",
                                    overflow: "auto",
                                  }}
                                >
                                  <div
                                    style={{
                                      marginBottom: "10px",
                                    }}>
                                    <img
                                      className="detail-image"
                                      src={image}
                                      width="300px"
                                      height="250px"
                                      alt={title}
                                    />
                                  </div>
                                  <div
                                    style={{
                                      fontFamily: "'Malgun Gothic', dotum, '돋움', sans-serif;line-height: 1.5",
                                      fontSize: "15px",
                                      color: "#888",
                                      marginTop: "-2px",
                                      overflow: "scroll",
                                      padding: "5px",
                                    }}>

                                    <div
                                      style={{
                                        padding: "5px 0 0 10px",
                                        height: "30px",
                                        background: "#6fddff",
                                        borderBottom: "1px solid #ddd",
                                        fontSize: "18px",
                                        fontWeight: "bold",
                                      }}>
                                      {title}
                                    </div>
                                    <br />
                                    <div>
                                      주소: {oAddress}
                                    </div>
                                    <br />

                                    <div>
                                      {name01}: {value01} <br />
                                      {value02} <br />
                                    </div>
                                    <br />

                                    <div>
                                      비용: {value03} <br />
                                    </div>

                                    <div>
                                      번호: {phone}
                                    </div>
                                  </div>
                                </div>

                                {/* 2번구역 */}
                                <div
                                  style={{
                                    border: "2px solid tomato",
                                    float: "left",
                                    width: "300px",
                                    height: "450px",
                                    margin: "10px",
                                    padding: "5px",
                                    // overflow: "auto",
                                  }}>

                                  <div
                                    style={{
                                      border: "2px solid aqua",
                                      width: "300px",
                                      height: "225px",
                                    }}>
                                    전체점수: {scoreTotal} <br />
                                    리뷰점수: {scoreReview}
                                  </div>

                                  <div
                                    style={{
                                      border: "2px solid gold",
                                      width: "300px",
                                      height: "225px",
                                    }}>

                                    {/* 그래프그리기 */}
                                    <div style={{ color: "blue", width: "300px", }}>
                                      각 장소별 편의지수 차트
                                    </div>


                                    <ResponsiveContainer>
                                      <RadarChart cx="50%" cy="50%" outerRadius="80%" width={300} height={200} data={data}>
                                        <PolarGrid />
                                        <PolarAngleAxis dataKey="subject" />
                                        <PolarRadiusAxis />
                                        <Radar name="점수" dataKey="score" stroke="#8884d8" fill="#8884d8" fillOpacity={0.6} />
                                      </RadarChart>
                                    </ResponsiveContainer>


                                  </div>
                                </div>

                                {/* 3번구역 */}
                                <div
                                  style={{
                                    border: "2px solid tomato",
                                    float: "left",
                                    width: "300px",
                                    height: "450px",
                                    margin: "10px",
                                    padding: "5px",
                                  }}>
                                  <div
                                    style={{
                                      border: "2px solid aqua",
                                      width: "300px",
                                      height: "225px",
                                    }}>워드클라우드
                                  </div>

                                  <div
                                    style={{
                                      border: "2px solid aqua",
                                      width: "300px",
                                      height: "225px",
                                    }}>
                                    행정구역과 비교 그래프
                                  </div>
                                </div>
                              </div>
                            </div>
                          </CustomOverlayMap>
                        )
                      }
                    </div>
                  </div>
                </div>
              </div>
            </CustomOverlayMap>
          )}

      </>
    )
  }


  return (
    // 사이드바
    <div className="all-contents">
      <div className="side-bar">
        <div className="container">
          <div style={{ width: isOpen ? "200px" : "50px" }} className="sidebar">
            <div className="top_section">
              <div style={{ marginLeft: "0px" }} className="bars">
                <FaBars onClick={toggle} />
              </div>
            </div>
            {
              menuItem.map((item, index) => (
                <div key={index} className="link" activeclassname="active">
                  <div className="icon" onClick={item.clicked}>{item.icon}</div>
                  <div style={{ display: isOpen ? "block" : "none" }} className="link_text">{item.name}</div>
                </div>
              ))
            }
          </div>
        </div>
      </div>


      <div className="map-area">
        
        <div>
          <div className="category">
            <ul>
              <li id="waterpark" onClick={() => setSelectedCategory("waterpark")}>
                <span className="ico_comm ico_waterpark"></span>
                물놀이장
              </li>
              <li id="fountain" onClick={() => setSelectedCategory("fountain")}>
                <span className="ico_comm ico_store"></span>
                바닥분수
              </li>
              <li id="pool" onClick={() => setSelectedCategory("pool")}>
                <span className="ico_comm ico_carpark"></span>
                수영
              </li>
            </ul>
          </div>
        </div>

        <div className="manual">
          <div style={{ color: '#3170B9'}}>
            <div style={{display: "flex", justifyContent:"center", alignItems:"center"}}>편의지수란? &nbsp; <img src="/image/bar.png"></img></div>
          </div>
        </div>


        <div className="map-wrap">
          <Map
            id={`map`}
            center={location.center}
            style={{
              // 지도의 크기
              width: "100vw",
              height: "100vh",
              // border: '2px solid #3170B9',
              borderRadius: '10px',
              marginLeft: '5px',
            }}
            level={3} // 지도의 확대 레벨
          >
            {/* 수유실 아이콘 클릭시 */}
            {/* {
            isNurseClick && (
              nurse.map((data) => (
                <MapMarker
                  key={`nurse-${data.toiletname}-${data.toiletla}-${data.toiletlo}`}
                  position={{ lat: data.toiletla, lng: data.toiletlo }}
                  image={{
                    src: 'https://cdn-icons-png.flaticon.com/128/469/469012.png',
                    size: {
                      width: 35,
                      height: 35
                    }
                  }}
                />
              ))
            )
          } */}
            {
              isNurseClick && (
                nurse.map((data) => (
                  <CustomOverlay
                    key={`${data.toiletid}`}
                    position={{ lat: data.toiletla, lng: data.toiletlo }}
                    image='https://cdn-icons-png.flaticon.com/128/469/469012.png'
                    title={data.toiletname}
                    address={data.toiletaddrold}
                    newAddress={data.toiletaddrnew}
                  />
                ))
              )

            }


            {/* 화장실 아이콘 클릭시 */}
            {/* {
            isToiletClick && (
              toilet.map((data) => (
                <MapMarker
                  key={`toilet-${data.toiletname}-${data.toiletla}-${data.toiletlo}`}
                  position={{ lat: data.toiletla, lng: data.toiletlo }}
                  image={{
                    src: 'https://cdn-icons-png.flaticon.com/128/325/325364.png',
                    size: {
                      width: 35,
                      height: 35
                    }
                  }}
                />
              ))
            )
          } */}

            {
              isToiletClick && (
                toilet.map((data) =>
                  <CustomOverlay
                    key={`toilet-${data.toiletname}-${data.toiletla}-${data.toiletlo}`}
                    position={{ lat: data.toiletla, lng: data.toiletlo }}
                    image='https://cdn-icons-png.flaticon.com/128/325/325364.png'
                    title={data.toiletname}
                    address={data.toiletaddrold}
                    newAddress={data.toiletaddrnew}
                  />
                )
              )
            }

            {
              isConvClick && (
                conv.map((data) => (
                  <CustomOverlay
                    key={`conv-${data.convname}-${data.convla}-${data.convlo}`}
                    position={{ lat: data.convla, lng: data.convlo }}
                    image='https://cdn-icons-png.flaticon.com/128/3733/3733125.png'
                    title={data.convname}
                    address={`${data.convsido} ${data.convsigngu} ${data.convdong}`}
                    newAddress={null}
                  />
                ))
              )
            }

            {/* 드러그스토어 아이콘 클릭시 */}
            {/* {
            isStoreClick && (
              store.map((data) => (
                <MapMarker
                  key={`store-${data.convname}-${data.convla}-${data.convlo}`}
                  position={{ lat: data.convla, lng: data.convlo }}
                  image={{
                    src: 'https://cdn-icons-png.flaticon.com/128/5790/5790819.png',
                    size: {
                      width: 35,
                      height: 35
                    }
                  }}
                />
              ))
            )
          } */}

            {
              isStoreClick && (
                store.map((data) => (
                  <CustomOverlay
                    key={`store-${data.convname}-${data.convla}-${data.convlo}`}
                    position={{ lat: data.convla, lng: data.convlo }}
                    image='https://cdn-icons-png.flaticon.com/128/5790/5790819.png'
                    title={data.convname}
                    address={`${data.convsido} ${data.convsigngu} ${data.convdong}`}
                    newAddress={null}
                  />
                ))
              )
            }

            {/* 약국 아이콘 클릭시 */}
            {
              isPillClick && (
                pill.map((data) => (
                  <MapMarker
                    key={`${data.mediid}-${data.mediname}-${data.medila}-${data.medilo}`}
                    position={{ lat: data.medila, lng: data.medilo }}
                    image={{
                      src: 'https://cdn-icons-png.flaticon.com/128/655/655968.png',
                      size: {
                        width: 35,
                        height: 35
                      }
                    }}
                  />
                ))
              )
            }

            {/* 병원 아이콘 클릭시 */}
            {
              isHospitalClick && (
                pill.map((data) => (
                  <MapMarker
                    key={`${data.mediid}-${data.mediname}-${data.medila}-${data.medilo}`}
                    position={{ lat: data.medila, lng: data.medilo }}
                    image={{
                      src: 'https://cdn-icons-png.flaticon.com/128/527/527034.png',
                      size: {
                        width: 35,
                        height: 35
                      }
                    }}
                  />
                ))
              )
            }

            {/* 경찰 아이콘 클릭시 */}
            {
              isPoliceClick && (
                police.map((data) => (
                  <MapMarker
                    key={`${data.safe112id}`}
                    position={{ lat: data.safe112la, lng: data.safe112lo }}
                    image={{
                      src: 'https://cdn-icons-png.flaticon.com/128/3025/3025649.png',
                      size: {
                        width: 35,
                        height: 35
                      }
                    }}
                  />
                ))
              )
            }

            {/* 소방서 아이콘 클릭시 */}
            {
              isFireClick && (
                fire.map((data) => (
                  <MapMarker
                    key={`${data.safe119id}`}
                    position={{ lat: data.safe119la, lng: data.safe119lo }}
                    image={{
                      src: 'https://cdn-icons-png.flaticon.com/128/2991/2991301.png',
                      size: {
                        width: 35,
                        height: 35
                      }
                    }}
                  />
                ))
              )
            }

            {/* 민영주차장 아이콘 클릭시 */}
            {/* {
            isParkClick && (
              park.map((data) => (
                <MapMarker
                  key={`${data.parkingid}`}
                  position={{ lat: data.parkingla, lng: data.parkinglo }}
                  image={{
                    src: 'https://cdn-icons-png.flaticon.com/128/4289/4289351.png',
                    size: {
                      width: 35,
                      height: 35
                    }
                  }}
                />
              ))
            )
          } */}
            {/* 공영주차장 아이콘 클릭시 */}
            {
              isFreeClick && (
                free.map((data) => (
                  <MapMarker
                    key={`${data.parkingid}`}
                    position={{ lat: data.parkingla, lng: data.parkinglo }}
                    image={{
                      src: 'https://cdn-icons-png.flaticon.com/128/2554/2554959.png',
                      size: {
                        width: 35,
                        height: 35
                      }
                    }}
                  />
                ))
              )
            }




            {/* 내위치표시 */}
            <MapMarker
              position={location.center}
              image={{
                src: 'https://cdn-icons-png.flaticon.com/128/4842/4842564.png',
                // src: {logo},
                size: {
                  width: 50,
                  height: 50
                }
              }}
            >내 위치요!</MapMarker>


            {/* 물놀이터 시설 위치 표시 */}
            {/* {selectedCategory === "waterpark" &&
            wptype1.map((data) => (
              <MapMarker
                key={`wptype1-${data.waterplayname}-${data.waterplayla}-${data.waterplaylo}`}
                position={{ lat: data.waterplayla, lng: data.waterplaylo }}
                image={
                  data.waterplayscorefacidesc == "red" ?
                    {
                      src: 'https://cdn-user-icons.flaticon.com/111444/111444393/1690870845646.svg?token=exp=1690871751~hmac=2bbed3916f4332ca8949d135de45045c',
                      size: {
                        width: 50,
                        height: 50

                      }
                    }
                    :
                    data.waterplayscorefacidesc == "blue" ?
                      {
                        src: 'https://cdn-user-icons.flaticon.com/111444/111444393/1690870813768.svg?token=exp=1690871719~hmac=277ef4859a8f3dbf4dc051d496101099',
                        size: {
                          width: 50,
                          height: 50

                        }
                      }
                      :
                      {
                        src: 'https://cdn-user-icons.flaticon.com/111444/111444393/1690870827290.svg?token=exp=1690871733~hmac=0528ab2840dffdb7015f3ef6bd08759d',
                        size: {
                          width: 50,
                          height: 50

                        }
                      }}
              />
            ))
          } */}

            {selectedCategory === "waterpark" &&
              wptype1.map((data) => (
                <WaterCustomOverlay
                  key={`wptype1-${data.waterplayname}-${data.waterplayla}-${data.waterplaylo}`}
                  position={{ lat: data.waterplayla, lng: data.waterplaylo }}
                  markerImage={
                    data.waterplayscorefacidesc == "red" ?
                      {
                        src: 'https://cdn-user-icons.flaticon.com/111444/111444393/1690870845646.svg?token=exp=1690871751~hmac=2bbed3916f4332ca8949d135de45045c',
                        size: {
                          width: 50,
                          height: 50

                        }
                      }
                      :
                      data.waterplayscorefacidesc == "blue" ?
                        {
                          src: 'https://cdn-user-icons.flaticon.com/111444/111444393/1690870813768.svg?token=exp=1690871719~hmac=277ef4859a8f3dbf4dc051d496101099',
                          size: {
                            width: 50,
                            height: 50

                          }
                        }
                        :
                        {
                          src: 'https://cdn-user-icons.flaticon.com/111444/111444393/1690870827290.svg?token=exp=1690871733~hmac=0528ab2840dffdb7015f3ef6bd08759d',
                          size: {
                            width: 50,
                            height: 50

                          }
                        }}
                  image={data.waterplayimgurl}
                  title={data.waterplayname}
                  oAddress={data.waterplayaddrold}
                  nAddress={data.waterplayaddrnew}
                  value01={data.waterplayvalue01}
                  value02={data.waterplayvalue02}
                  value03={data.waterplayvalue03}
                  name01={data.waterplayname01}
                  phone={data.waterplaytelno}
                  scoreToilet={data.waterplayscoretoilet}
                  scoreConv={data.waterplayscoreconv}
                  scoreDrug={data.waterplayscoredrug}
                  scoreMedi={data.waterplayscoremedi}
                  score112={data.waterplayscoresafe112}
                  score119={data.waterplayscoresafe119}
                  scorePark={data.waterplayscoreparking}
                  scoreTotal={data.waterplayscorefaci}
                  scoreColor={data.waterplayscorefacidesc}
                  scoreReview={data.waterplayscorereview}
                />
              ))
            }



            {/* 수영 시설 위치 표시 */}
            {/* {selectedCategory === "pool" &&
            wptype2.map((data) => (
              <MapMarker
                key={`wptype2-${data.waterplayname}-${data.waterplayla}-${data.waterplaylo}`}
                position={{ lat: data.waterplayla, lng: data.waterplaylo }}
                image={
                  data.waterplayscorefacidesc == "red" ?
                    {
                      src: 'https://cdn-user-icons.flaticon.com/111444/111444393/1690871094686.svg?token=exp=1690872000~hmac=8c0487151640de418d9a99af8de5ca2e',
                      size: {
                        width: 50,
                        height: 50

                      }
                    }
                    :
                    data.waterplayscorefacidesc == "blue" ?
                      {
                        src: 'https://cdn-user-icons.flaticon.com/111444/111444393/1690871131678.svg?token=exp=1690872038~hmac=86bcd8a62b55d060f3771f91f8b45cb6',
                        size: {
                          width: 50,
                          height: 50

                        }
                      }
                      :
                      {
                        src: 'https://cdn-user-icons.flaticon.com/111444/111444393/1690871165328.svg?token=exp=1690872070~hmac=9a223618ab42ae4131ccd39b01ed6331',
                        size: {
                          width: 50,
                          height: 50

                        }
                      }
                }
              >
              </MapMarker>
            ))
          } */}

            {/* 수영 시설 위치 표시 */}
            {selectedCategory === "pool" &&
              wptype2.map((data) => (
                <WaterCustomOverlay
                  key={`wptype2-${data.waterplayname}-${data.waterplayla}-${data.waterplaylo}`}
                  position={{ lat: data.waterplayla, lng: data.waterplaylo }}
                  markerImage={
                    data.waterplayscorefacidesc == "red" ?
                      {
                        src: 'https://cdn-user-icons.flaticon.com/111444/111444393/1690871094686.svg?token=exp=1690872000~hmac=8c0487151640de418d9a99af8de5ca2e',
                        size: {
                          width: 50,
                          height: 50

                        }
                      }
                      :
                      data.waterplayscorefacidesc == "blue" ?
                        {
                          src: 'https://cdn-user-icons.flaticon.com/111444/111444393/1690871131678.svg?token=exp=1690872038~hmac=86bcd8a62b55d060f3771f91f8b45cb6',
                          size: {
                            width: 50,
                            height: 50

                          }
                        }
                        :
                        {
                          src: 'https://cdn-user-icons.flaticon.com/111444/111444393/1690871165328.svg?token=exp=1690872070~hmac=9a223618ab42ae4131ccd39b01ed6331',
                          size: {
                            width: 50,
                            height: 50

                          }
                        }
                  }
                  image={data.waterplayimgurl}
                  title={data.waterplayname}
                  oAddress={data.waterplayaddrold}
                  nAddress={data.waterplayaddrnew}
                  value01={data.waterplayvalue01}
                  value02={data.waterplayvalue02}
                  value03={data.waterplayvalue03}
                  phone={data.waterplaytelno}
                  scoreToilet={data.waterplayscoretoilet}
                  scoreConv={data.waterplayscoreconv}
                  scoreDrug={data.waterplayscoredrug}
                  scoreMedi={data.waterplayscoremedi}
                  score112={data.waterplayscoresafe112}
                  score119={data.waterplayscoresafe119}
                  scorePark={data.waterplayscoreparking}
                  scoreTotal={data.waterplayscorefaci}
                  scoreColor={data.waterplayscorefacidesc}
                  scoreReview={data.waterplayscorereview}
                >
                </WaterCustomOverlay>
              ))
            }

            {/* 바닥분수 위치표시 */}
            {/* {
            selectedCategory === "fountain" &&
            wptype3.map((data) => (
              <MapMarker
                key={`wptype3-${data.waterplayname}-${data.waterplayla}-${data.waterplaylo}`}
                position={{ lat: data.waterplayla, lng: data.waterplaylo }}
                image={data.waterplayscorefacidesc == "red" ?
                  {
                    src: 'https://cdn-user-icons.flaticon.com/111444/111444393/1690870990817.svg?token=exp=1690871896~hmac=7ea272c92ef582d7cb83b9d10c2a6517',
                    size: {
                      width: 50,
                      height: 50

                    }
                  }
                  :
                  data.waterplayscorefacidesc == "blue" ?
                    {
                      src: 'https://cdn-user-icons.flaticon.com/111444/111444393/1690871025190.svg?token=exp=1690871930~hmac=821f00b9806c218419fafed96bef6fef',
                      size: {
                        width: 50,
                        height: 50

                      }
                    }
                    :
                    {
                      src: 'https://cdn-user-icons.flaticon.com/111444/111444393/1690871047538.svg?token=exp=1690871953~hmac=cce9688494742c4203ea76cd881418c5',
                      size: {
                        width: 50,
                        height: 50

                      }
                    }}
              >
              </MapMarker>
            ))
          } */}

            {
              selectedCategory === "fountain" &&
              wptype3.map((data) => (
                <WaterCustomOverlay
                  key={`wptype3-${data.waterplayname}-${data.waterplayla}-${data.waterplaylo}`}
                  position={{ lat: data.waterplayla, lng: data.waterplaylo }}
                  markerImage={data.waterplayscorefacidesc == "red" ?
                    {
                      src: 'https://cdn-user-icons.flaticon.com/111444/111444393/1690870990817.svg?token=exp=1690871896~hmac=7ea272c92ef582d7cb83b9d10c2a6517',
                      size: {
                        width: 50,
                        height: 50

                      }
                    }
                    :
                    data.waterplayscorefacidesc == "blue" ?
                      {
                        src: 'https://cdn-user-icons.flaticon.com/111444/111444393/1690871025190.svg?token=exp=1690871930~hmac=821f00b9806c218419fafed96bef6fef',
                        size: {
                          width: 50,
                          height: 50

                        }
                      }
                      :
                      {
                        src: 'https://cdn-user-icons.flaticon.com/111444/111444393/1690871047538.svg?token=exp=1690871953~hmac=cce9688494742c4203ea76cd881418c5',
                        size: {
                          width: 50,
                          height: 50

                        }
                      }}
                  image={data.waterplayimgurl}
                  title={data.waterplayname}
                  oAddress={data.waterplayaddrold}
                  nAddress={data.waterplayaddrnew}
                  value01={data.waterplayvalue01}
                  value02={data.waterplayvalue02}
                  value03={data.waterplayvalue03}
                  phone={data.waterplaytelno}
                  scoreToilet={data.waterplayscoretoilet}
                  scoreConv={data.waterplayscoreconv}
                  scoreDrug={data.waterplayscoredrug}
                  scoreMedi={data.waterplayscoremedi}
                  score112={data.waterplayscoresafe112}
                  score119={data.waterplayscoresafe119}
                  scorePark={data.waterplayscoreparking}
                  scoreTotal={data.waterplayscorefaci}
                  scoreColor={data.waterplayscorefacidesc}
                  scoreReview={data.waterplayscorereview}
                >
                </WaterCustomOverlay>
              ))
            }
          </Map>
        </div>
      </div>
      {/* 
      <div className="category">
        <ul>
          <li id="waterpark" onClick={() => setSelectedCategory("waterpark")}>
            <span className="ico_comm ico_waterpark"></span>
            물놀이장
          </li>
          <li id="fountain" onClick={() => setSelectedCategory("fountain")}>
            <span className="ico_comm ico_store"></span>
            바닥분수
          </li>
          <li id="pool" onClick={() => setSelectedCategory("pool")}>
            <span className="ico_comm ico_carpark"></span>
            수영
          </li>
        </ul>
      </div> */}

    </div>
  )
};

export default ChildMap;