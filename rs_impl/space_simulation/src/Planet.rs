use super::VectorMath as vm;

const GRAV_CONST: f32 = 0.0001; 

pub struct Planet {
    pub v: [f32; 2],
    pub pos: [f32; 2],
    pub name: String,
    pub color: (u8, u8, u8),
    pub radius: i16,
    pub surface_grav: f32,
}

impl Planet {
    pub fn get_radius(&self) -> i16 {
        return self.radius;
    }

    pub fn get_pos(&self) -> Vec<f32> {
        Vec::from(self.pos)
    }

    pub fn set_pos(&mut self, x: f32, y: f32) {
        self.pos = [x, y];
    }

    pub fn get_color(&self) -> (u8, u8, u8) {
        self.color
    }

    pub fn set_color(&mut self, color: (u8, u8, u8)) {
        self.color = color;
    }

    pub fn get_mass(&self) -> f32 {
        self.surface_grav * self.radius as f32 * self.radius as f32 / GRAV_CONST
    }

    pub fn get_vel(&self) -> Vec<f32> {
        let temp = Vec::from(self.v);
        vm::vec_nrm(temp)
    }

    pub fn update_velocity(&mut self, all_planets: Vec<Planet>, time_step: f32) {
        for planet in all_planets.iter() {
            let dst_sqr: f32 = vm::vec_dst(planet.get_pos(), self.get_pos());
            let force_dir: Vec<f32> = vm::vec_nrm(match vm::vec_sub(planet.get_pos(), self.get_pos()) {
                Some(v) => Vec::from(v),
                None => Vec::from([0., 0.])
            });
            // F = Gmm/r^2
            let force: Vec<f32> = vm::vec_mul(force_dir, GRAV_CONST * self.get_mass() * planet.get_mass() / dst_sqr);
            let acceleration: Vec<f32> = vm::vec_mul(force, self.get_mass());
            let temp: Vec<f32> = vm::vec_mul(acceleration, time_step);
            self.v[0] += temp[0];
            self.v[1] += temp[1];
        }
    }
}
