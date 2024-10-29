import * as THREE from 'three'; 
import ThreeGlobe from 'three-globe';


const scene = new THREE.Scene(); 
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 ); 
const renderer = new THREE.WebGLRenderer(); renderer.setSize( window.innerWidth, window.innerHeight ); 
renderer.setAnimationLoop( animate ); 

document.body.appendChild( renderer.domElement ); 

const myGlobe = new ThreeGlobe()
  .globeImageUrl(myImageUrl)
  .pointsData(myData);

const myScene = new THREE.Scene();
scene.add(myGlobe);

function animate() {
    renderer.render( scene, camera ); 
}
