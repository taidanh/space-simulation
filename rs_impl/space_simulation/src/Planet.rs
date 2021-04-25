pub struct Planet {
    pub v: [f32; 2],
    pub pos: [f32; 2],
    pub name: String,
    pub color: [i8; 3],
    pub radius: i16,
    pub surface_grav: f32,
}

impl Planet {
    fn get_radius(&self) -> i16 {
        return self.radius;
    }

    pub fn get_pos(&self) -> (f32, f32) {
        (self.pos[0], self.pos[1])
    }
}