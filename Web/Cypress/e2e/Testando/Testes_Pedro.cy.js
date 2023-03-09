describe('My First Test', () => {
    it('clicking "type" navigates to a new url', () => {
        cy.visit('https://music.youtube.com/channel/UC0TVdBsW4LmqasScQqRJ7FA')

        let x = cy.get('.content-container > .title')
        x.should('have.value', 'Belik Boom')

        console.log(x)
    })
})