
export default function Bento({children}) {
  return (
    <div className='Bento'
      alignItems="center"
      style={
        {
        width: '300px',
        border: '2px solid black',
        borderBottomLeftRadius: '30px',
        borderBottomRightRadius: '30px',
        borderTopLeftRadius: '30px',
        borderTopRightRadius: '30px'}} >
      {children}
    </div>
  );
}
