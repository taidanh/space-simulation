//----------------------//
//      MATH STUFF      //
//----------------------//

pub fn vec_add(v1: Vec<f32>, v2: Vec<f32>) -> Option<Vec<f32>> {
    let mut new: Vec<f32> = Vec::new();
    if v1.len() == v2.len() {
        for i in 0..v1.len() {
            new.push(v1[i] + v2[i]);
        }
    }
    match new.len() {
        0 => None,
        _ => Some(new)
    }
}

pub fn vec_sub(v1: Vec<f32>, v2: Vec<f32>) -> Option<Vec<f32>> {
    let mut new: Vec<f32> = Vec::new();
    if v1.len() == v2.len() {
        for i in 0..v1.len() {
            new.push(v1[i] - v2[i]);
        }
    }
    match new.len() {
        0 => None,
        _ => Some(new)
    }
}

pub fn vec_sqt(x: Vec<f32>) -> Vec<f32> {
    let mut new: Vec<f32> = Vec::new();
    for i in x {
        new.push(i.sqrt());
    }
    new
}

pub fn vec_mul(v: Vec<f32>, scalar: f32) -> Vec<f32> {
    let mut new:Vec<f32> = Vec::new();
    for i in v {
        new.push(i * scalar);
    }
    new
}

pub fn vec_div(v: Vec<f32>, scalar: f32) -> Vec<f32> {
    let mut new: Vec<f32> = Vec::new();
    for i in v {
        new.push(i / scalar);
    }
    new
}

pub fn vec_pow(v: Vec<f32>, power: f32) -> Vec<f32> {
    let mut new: Vec<f32> = Vec::new();
    for i in v {
        new.push(i.powf(power));
    }
    new
}

pub fn vec_mag(v: Vec<f32>) -> f32 {
    let mut sum: f32 = 0.0;
    for i in v {
        sum += i.powf(2.0);
    }
    sum.sqrt()
}

pub fn vec_dst(v1: Vec<f32>, v2: Vec<f32>) -> f32 {
    let mut sum: f32 = 0.0;
    if v1.len() == v2.len() {
        for i in 0..v1.len() {
            sum += (v1[i] - v2[i]).powf(2.0);
        }
    }
    sum
}

pub fn vec_nrm(v: Vec<f32>) -> Vec<f32> {
    vec_div(v, vec_mag(v))
}
