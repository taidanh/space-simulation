pub mod Planet;
pub mod VectorMath;

fn main() {
    println!("Hello, world!");
    let p1 = Planet::Planet {
        pos: [12.0, 155.0],
        v: [100.0, -150.0],
        name: String::from("first"),
        color: (115, 115, 115),
        radius: 30,
        surface_grav: 123.45
    };
    println!("the position of {} is {:?}", p1.name, p1.get_pos());
}
